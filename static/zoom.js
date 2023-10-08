const galleryImages = document.querySelectorAll('.gallery__img');

// Get the enlarged image container and the enlarged image element
const enlargedImageContainer = document.querySelector('.enlarged-image-container');
const enlargedImage = document.querySelector('.enlarged-image');

// Add click event listener to each gallery image
galleryImages.forEach(image => {
  image.addEventListener('click', () => {
    // Set the source of the enlarged image to the clicked image's source
    enlargedImage.src = image.src;
    enlargedImage.alt = image.alt;

    // Display the enlarged image container
    enlargedImageContainer.style.display = 'block';
  });
});

// Add click event listener to the enlarged image container to close it
enlargedImageContainer.addEventListener('click', () => {
  // Hide the enlarged image container when clicked
  enlargedImageContainer.style.display = 'none';
});