document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // prevent immediate form submission

        // Create and show "thinking" box
        let thinkingBox = document.createElement('div');
        thinkingBox.className = 'response-box thinking';
        thinkingBox.textContent = 'AI is thinking...';

        // Append the thinking box just below the form
        form.parentNode.appendChild(thinkingBox);

        // Now submit the form normally
        form.submit();
    });
});
