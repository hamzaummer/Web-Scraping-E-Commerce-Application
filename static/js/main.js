// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Handle export button click
    const exportBtn = document.querySelector('a[href*="export"]');
    if (exportBtn) {
        exportBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('href');
            
            // Show loading indicator
            const originalText = this.innerHTML;
            this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Exporting...';
            this.disabled = true;
            
            // Make AJAX request
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Create a download link
                        const a = document.createElement('a');
                        a.href = data.filename;
                        a.download = data.filename;
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);
                        
                        // Show success message
                        alert('Data exported successfully!');
                    } else {
                        alert('Export failed: ' + (data.message || 'Unknown error'));
                    }
                })
                .catch(error => {
                    console.error('Export error:', error);
                    alert('Export failed. Please try again.');
                })
                .finally(() => {
                    // Restore button
                    this.innerHTML = originalText;
                    this.disabled = false;
                });
        });
    }
    
    // Add Bootstrap icons
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css';
    document.head.appendChild(link);
    
    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});