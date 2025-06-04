<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Rhythm Booster">
  <link rel="manifest" href="manifest.json">
  <title>Rhythm Booster</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background: #f5f5f5;
      margin: 0;
      padding: 20px;
      text-align: center;
    }
    .task-box {
      background: white;
      padding: 20px;
      border-radius: 16px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
    button {
      padding: 12px 24px;
      font-size: 16px;
      border: none;
      border-radius: 8px;
      background-color: #4CAF50;
      color: white;
      cursor: pointer;
      margin: 5px;
    }
    button:hover {
      background-color: #45a049;
    }
    .quote {
      margin-top: 20px;
      font-style: italic;
    }
    .theme-switcher {
      margin-top: 30px;
    }

    /* Responsive for small screens */
    @media (max-width: 600px) {
      body {
        padding: 10px;
      }
      .task-box {
        padding: 15px;
      }
      button {
        width: 90%;
        font-size: 18px;
      }
    }
  </style>
</head>
<body>
  <div class="task-box">
    <h2>今日任務</h2>
    <p id="task">看教學影片 5 分鐘</p>
    <button onclick="completeTask()">完成！</button>
    <p class="quote" id="quote"></p>
  </div>

  <div class="theme-switcher">
    <p>切換風格：</p>
    <button onclick="setTheme('playful')">🎮 遊戲</button>
    <button onclick="setTheme('minimal')">🧘 簡約</button>
    <button onclick="setTheme('techy')">💻 工程</button>
  </div>

  <audio id="bg-music" src="https://www.bensound.com/bensound-music/bensound-dreams.mp3" loop></audio>

  <script>
    const quotes = [
      "行動是治癒焦慮的良藥，而不是思考。",
      "你不需要一次完成所有，只需要開始。",
      "做比完美更重要。",
      "今天做一點，明天會更容易。",
    ];

    function completeTask() {
      const quote = quotes[Math.floor(Math.random() * quotes.length)];
      document.getElementById('quote').innerText = quote;
      document.getElementById('bg-music').play();
    }

    function setTheme(theme) {
      switch (theme) {
        case 'playful':
          document.body.style.background = '#ffeaa7';
          break;
        case 'minimal':
          document.body.style.background = '#ecf0f1';
          break;
        case 'techy':
          document.body.style.background = '#2c3e50';
          document.body.style.color = '#ecf0f1';
          break;
      }
    }
  </script>
</body>
</html>
