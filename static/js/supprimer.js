function confirmerSuppression(event) {
    // Afficher une boîte de confirmation
    const confirmation = confirm("Attention, vous êtes sur le point de supprimer cet élève ! Voulez-vous vraiment continuer ?");

    // Si l'utilisateur clique sur "OK", on permet la soumission du formulaire
    return confirmation;
}