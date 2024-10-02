document.getElementById('verifyUserBtn').addEventListener('click', function() {
    const userId = document.getElementById('userId').value;
    fetch('/api/verify_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: userId })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('userResult').innerText = JSON.stringify(data);
    });
});

document.getElementById('verifyVideoBtn').addEventListener('click', function() {
    const videoId = document.getElementById('videoId').value;
    fetch('/api/verify_video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ video_id: videoId })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('videoResult').innerText = JSON.stringify(data);
    });
});
