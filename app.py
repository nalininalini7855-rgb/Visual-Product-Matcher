<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Knowledge-base Search Engine</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <div class="container">
    <h2>📚 Visual Product Matcher</h2>

    <form id="uploadForm">
      <input type="file" name="file" required>
      <button type="submit">Upload</button>
    </form>

    <hr>

    <form id="questionForm">
      <input type="text" id="query" placeholder="Ask a question..." required>
      <button type="submit">Ask</button>
    </form>

    <div id="answerBox">✅ File uploaded and processed successfully!</div>
  </div>

  <script>
    const answerBox = document.getElementById("answerBox");

    // Upload form
    document.getElementById("uploadForm").onsubmit = async (e) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const res = await fetch("/upload", { method: "POST", body: formData });
      const data = await res.json();

      if (data.status === "success") {
        answerBox.innerText = `✅ File uploaded and processed successfully! (${data.vectors_added} vectors added)`;
      } else {
        answerBox.innerText = `❌ ${data.error}`;
      }
    };

    // Question form
    document.getElementById("questionForm").onsubmit = async (e) => {
      e.preventDefault();
      const query = document.getElementById("query").value;
      const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
      });
      const data = await res.json();
      answerBox.innerText = data.answer || `❌ ${data.error}`;
    };
  </script>
</body>
</html>
