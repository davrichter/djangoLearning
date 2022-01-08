export function loadToolTips() {
    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    let tooltipList = tooltipTriggerList.map( (tooltipTriggerEl) => {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
}