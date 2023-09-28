async function generatePost() {
    console.log("Sending input to server for text generation.");
    const userInput = document.getElementById("userInput").value;
    const response = await fetch('/generate', {
        method: 'POST',
        body: JSON.stringify({ input: userInput }),
        headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();
    console.log("Received generated text from server: ", data.output);
    document.getElementById("generatedText").innerText = data.output;
}

async function postToTwitter() {
    console.log("Sending confirmed text to server for posting to Twitter.");
    const confirmedText = document.getElementById("generatedText").innerText;
    const response = await fetch('/postToTwitter', {
        method: 'POST',
        body: JSON.stringify({ confirmedText }),
        headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();
    console.log("Received server confirmation: ", data.status);
    alert(data.status);
}
