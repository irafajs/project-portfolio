document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.delete').forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault();
            const medId = this.closest('tr').querySelector('.med-id').value;
            deleteMedicine(medId);
        });
    });
    
    function deleteMedicine(medId) {
        fetch(`/delete/${medId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            window.location.href = "/admin_profile";
            alert(`${data.med_name} deleted successfully`); 
        })
        .catch(error => {
            console.error('There was an error!', error);
        });
    }
});
