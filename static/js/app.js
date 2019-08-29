let heart = document.querySelector('.far');
heart.addEventListener('click', function(evt) {
  evt.preventDefault();
  heart.classList.toggle('far');
  heart.classList.toggle('fas');
})