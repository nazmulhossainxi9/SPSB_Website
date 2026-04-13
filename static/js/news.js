
function openModal{{ post.id }}(){
    var modal = new bootstrap.Modal(document.getElementById('modal{{ post.id }}'));
    modal.show();
}