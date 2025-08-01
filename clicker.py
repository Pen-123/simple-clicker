from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Clicker</title>
<style>
  body {
    margin: 0;
    font-family: sans-serif;
    background: #111;
    color: #0f0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh
  }
  button {
    padding: 1em 2em;
    font-size: 2em;
    border: none;
    border-radius: .3em;
    cursor: pointer;
    background: #222;
    color: #0f0;
    transition: transform .05s
  }
  button:active {
    transform: scale(.95)
  }
  span {
    font-size: 6rem
  }
</style>

<span id="n">0</span>
<button onclick="c()">Click</button>
<audio id="a" src="data:audio/wav;base64,UklGRn9GAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YR9GAACBhYqFbF1fdHx1cWxpZGNHRkhVTlZUXGx3fIeMlZ2mpKGcm5eUk46NioqEg4F8e3l3dnRzcnFvb25tbGtqaWhnZmVlZGNiYWBgX15dXFtbWlloaXZ7hY6ZoKessLW5trCtq6ShoJ6cm5mYl5aUk5GQj46NjIuKiYiHhoWEg4KBgIB/fn18e3p5eHd2dXRzcnFwb25tbGtqaWhnZmVkY2JhYF9eXVxbWllYV1ZVVFNSUVBPTk1MS0pJSEdGRURDQkFAPz49PDs6OTg3NjU0MzIxMC8uLSwrKikoJyYlJCMiISAfHh0cGxoZGBcWFRQTEhEQDw4NDAsKCQgHBgUEAwIBAHdpWEY7MS0qJSMgHhwaGRYVEhAPEAoHBgUDAQD9+vn49/b08O/t6+np5+bl5OLh39/e3dzb2tnZ2NfW1dTT0tHQz8/OzczLysnIx8bFxMTDwsHAv769vLu6ubi3trW0s7KxsK+uraysq6qpqKempaSjoqGgn56dnJuamZiXlpWUk5KRkI+OjYyLiomIh4aFhIOCgYCAfn59fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk5ODc2NTQzMjEwLy4tLCsqKSgnJiUkIyIhIB8eHRwbGhkYFxYVFBMSERAPDg0MCwoJCAcGBQQDAgEA" preload="auto"></audio>
<script>
  let n = 0;
  const el = document.getElementById('n');
  const a = document.getElementById('a');

  function c() {
    a.currentTime = 0; // rewind the sound
    a.play().catch(e => console.log("Audio play error:", e));
    let target = n + 10;
    let t = setInterval(() => {
      el.textContent = n;
      n++;
      if (n >= target) clearInterval(t);
    }, 40);
  }
</script>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
