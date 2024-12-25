document.querySelector('#comment-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    const response = await fetch(event.target.action, {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const newComment = await response.text();
        document.querySelector('#comments-list').innerHTML += newComment;
        event.target.reset();
    } else {
        alert('Error submitting comment!');
    }
});
