document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.form');
  const submitButton = form.querySelector('button[type="button"]');
  const messageInput = document.getElementById('message');

  submitButton.disabled = false;
  submitButton.style.pointerEvents = 'auto';


  submitButton.addEventListener('mouseenter', () => {
    submitButton.style.backgroundColor = '#4CAF50';
    submitButton.style.color = 'white';
  });

  submitButton.addEventListener('mouseleave', () => {
    submitButton.style.backgroundColor = 'white';
    submitButton.style.color = 'black';
  });

  submitButton.addEventListener('mousedown', () => {
    submitButton.style.backgroundColor = '#2e7d32';
    submitButton.style.color = 'white';
  });

  submitButton.addEventListener('mouseup', () => {
    submitButton.style.backgroundColor = '#4CAF50';
    submitButton.style.color = 'white';
  });

  submitButton.addEventListener('click', () => {
    if (messageInput.value.trim() === '') {
      alert('Please enter a message before submitting.');
      messageInput.focus();
      return;
    }

    alert('Message sent');


    messageInput.value = '';


    submitButton.style.backgroundColor = 'white';
    submitButton.style.color = 'black';
  });
});