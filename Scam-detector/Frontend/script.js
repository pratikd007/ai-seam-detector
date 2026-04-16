async function checkScam() {
    const message = document.getElementById("message").value;

    if (!message.trim()) {
        document.getElementById("result").innerText = "Please enter a message";
        return;
    }

    // Loading state (UX boost)
    document.getElementById("result").innerText = "Analyzing scam risk...";
    document.getElementById("result").style.opacity = "0.6";

    try {
        const response = await fetch("http://127.0.0.1:5000/check", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Show result
        document.getElementById("result").innerText =
            `${data.result} (Risk: ${data.score}%)`;

        document.getElementById("result").style.opacity = "1";

        // Confidence text (if added in backend)
        if (data.confidence) {
            document.getElementById("confidence").innerText = data.confidence;
        }

        // Progress bar
        const bar = document.getElementById("bar");
        bar.style.width = data.score + "%";

        // Color + glow effect
        const box = document.getElementById("resultBox");
        box.classList.remove("scam", "safe");

        if (data.result === "SCAM") {
            bar.style.background = "red";
            document.getElementById("result").style.color = "#ff4b2b";
            box.classList.add("scam");
        } else {
            bar.style.background = "limegreen";
            document.getElementById("result").style.color = "lightgreen";
            box.classList.add("safe");
        }

    } catch (error) {
        document.getElementById("result").innerText =
            "Error connecting to server";
        console.error(error);
    }
}


/* 🎤 VOICE INPUT FEATURE */
function startVoice() {
    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Voice input not supported in this browser");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function (event) {
        const text = event.results[0][0].transcript;
        document.getElementById("message").value = text;
    };
}