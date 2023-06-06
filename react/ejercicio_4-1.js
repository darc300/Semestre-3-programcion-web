//este codigo es la galeria de imagenes estaticas 
import React from 'react';

const ImageGallery = () => {
  const images = [
    {
      id: 1,
      src: '/images/image1.jpg',
      alt: 'Image 1',
    },
    {
      id: 2,
      src: '/images/image2.jpg',
      alt: 'Image 2',
    },
    {
      id: 3,
      src: '/images/image3.jpg',
      alt: 'Image 3',
    },
  ];

  return (
    <div className="image-gallery">
      {images.map((image) => (
        <img key={image.id} src={image.src} alt={image.alt} />
      ))}
    </div>
  );
};

export default ImageGallery;
