document.addEventListener("DOMContentLoaded", function() {
    const errorAlert = document.querySelector('.alert-error');
    const successAlert = document.querySelector('.alert-success');

    setTimeout(() => {
        errorAlert.classList.add('fade-out');
        successAlert.classList.add('fade-out');
    }, 1000); 
});
