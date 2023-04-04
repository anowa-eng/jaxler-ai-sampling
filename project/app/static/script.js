let prompt = document.getElementById('prompt'),
  response = document.getElementById('response');

$(prompt).on('input', () => {
    $('#prompt-value').attr('value', $(prompt).text());
});
$(response).on('input', () => {
    $('#response-value').attr('value', $(response).text());
});
