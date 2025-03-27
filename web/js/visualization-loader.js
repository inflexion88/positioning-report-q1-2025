document.addEventListener('DOMContentLoaded', function() {
  // Tab switching functionality
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Remove active class from all buttons and contents
      tabButtons.forEach(btn => btn.classList.remove('active'));
      tabContents.forEach(content => content.classList.remove('active'));
      
      // Add active class to clicked button
      button.classList.add('active');
      
      // Show corresponding content
      const tabId = button.getAttribute('data-tab');
      document.getElementById(tabId).classList.add('active');
    });
  });
  
  // Preload images for smoother experience
  const preloadImages = () => {
    const images = [
      'visualizations/gravitational_model_3d.gif',
      'visualizations/positioning_quadrants.png',
      'visualizations/development_pathway.png'
    ];
    
    images.forEach(src => {
      const img = new Image();
      img.src = src;
    });
  };
  
  preloadImages();
});
