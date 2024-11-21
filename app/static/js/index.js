function copiarTexto(texto) {
    navigator.clipboard.writeText(texto)
        .then(() => alert(`Texto copiado: ${texto}`))
        .catch(err => console.error('Error al copiar texto: ', err));
}