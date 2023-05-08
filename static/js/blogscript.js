$(document).ready(function() {
    $('.blog-post').each(function() {
      $(this).find('h3').wrap('<a href="#"></a>');
      $(this).find('.meta').prepend('<i class="far fa-clock"></i> ');
    });
  });
  