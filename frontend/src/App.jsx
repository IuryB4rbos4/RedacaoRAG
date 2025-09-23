import { useState } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";

function App() {
  const [essay, setEssay] = useState("");
  const [loading, setLoading] = useState(false);
  const [feedback, setFeedback] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setFeedback(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: essay }),
      });

      if (!response.ok) {
        throw new Error("Erro ao processar a redação");
      }

      const data = await response.json();
      setFeedback(data.feedback || data);
    } catch (error) {
      setFeedback({ error: error.message });
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1 className="title">O Sensacional Corretor de Redação</h1>

      <form onSubmit={handleSubmit} className="form-container">
        <textarea
          value={essay}
          onChange={(e) => setEssay(e.target.value)}
          placeholder="Cole sua redação aqui..."
          className="essay-input"
          required
        />
        <button
          type="submit"
          className="submit-btn"
          disabled={loading}
        >
          {loading ? "Analisando..." : "Enviar para Análise"}
        </button>
      </form>

      {feedback && (
        <div className="feedback-box">
          <h2 className="feedback-title">Feedback:</h2>
          <pre className="feedback-content">
            <ReactMarkdown>
              {typeof feedback === "string"
                ? feedback
                : JSON.stringify(feedback, null, 2)}
            </ReactMarkdown>
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;
