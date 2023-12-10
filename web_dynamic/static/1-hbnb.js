// static/scripts/1-hbnb.js

$(document).ready(function() {
  // Your JavaScript code here, executed when DOM is loaded

  // Listen for changes on each input checkbox tag
  $('input[type="checkbox"]').change(function() {
    // Initialize an empty array to store Amenity IDs
    var amenityIds = [];

    // Loop through each checked checkbox and store the Amenity ID
    $('input[type="checkbox"]:checked').each(function() {
      amenityIds.push($(this).data('id'));
    });

    // Update the h4 tag inside the div Amenities with the list of Amenities checked
    $('.popover h4').text('Amenities: ' + amenityIds.join(', '));
  });
});
