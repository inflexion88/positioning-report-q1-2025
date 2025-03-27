# Gravitational Authority Model - GitHub Deployment Guide

This guide provides step-by-step instructions for deploying the Gravitational Authority Model visualization and report package from GitHub.

## Repository Contents

```
gravitational-authority-model/
├── README.md                           # Project overview and documentation
├── reports/                            # Positioning reports
│   ├── final_q1_2025_positioning_report.md
│   ├── q1_2025_positioning_insights.md
│   └── q1_2025_market_analysis.md
├── visualization/                      # Visualization components
│   ├── improved_gravitational_model.py # Python script for generating visualizations
│   └── requirements.txt                # Python dependencies
├── web/                                # Web implementation files
│   ├── index.html                      # Main HTML file with visualization integration
│   ├── css/
│   │   └── styles.css                  # Styling for visualization components
│   ├── js/
│   │   └── visualization-loader.js     # JavaScript for visualization interaction
│   └── visualizations/                 # Directory for generated visualization files
└── docs/                               # Documentation
    └── upgrade.md                      # Implementation and customization guide
```

## Quick Start Guide

### Option 1: View the Pre-Generated Web Version

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gravitational-authority-model.git
   cd gravitational-authority-model
   ```

2. Open `web/index.html` in your browser to view the pre-generated visualizations and report.

### Option 2: Generate Fresh Visualizations

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gravitational-authority-model.git
   cd gravitational-authority-model
   ```

2. Install Python dependencies:
   ```bash
   pip install -r visualization/requirements.txt
   ```

3. Run the visualization script:
   ```bash
   cd visualization
   python improved_gravitational_model.py
   ```

4. Copy the generated files to the web directory:
   ```bash
   cp -r visualization_output/* ../web/visualizations/
   ```

5. Open `web/index.html` in your browser to view the visualizations with the report.

## Deployment Options

### GitHub Pages Deployment

1. Push the repository to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Enable GitHub Pages in your repository settings:
   - Go to Settings > Pages
   - Select "main" branch and "/web" folder as the source
   - Click Save

3. Your site will be published at `https://yourusername.github.io/gravitational-authority-model/`

### Custom Web Server Deployment

1. Upload the contents of the `web` directory to your web server using FTP or your preferred method.

2. Ensure the server has the correct permissions set for the files and directories.

3. Access your site at your domain or server address.

## Customization

### Modifying Company Data

1. Open `visualization/improved_gravitational_model.py`
2. Locate the `companies` array (around line 100)
3. Modify the company names and their positioning values
4. Re-run the script to generate updated visualizations

Example:
```python
companies = [
    ["Your Company", [0.9, 0.8, 0.7, 0.9, 0.8]],
    ["Competitor A", [0.7, 0.6, 0.8, 0.5, 0.7]],
    # Add more companies as needed
]
```

### Customizing Visual Appearance

1. Modify `web/css/styles.css` to match your brand colors and styling preferences
2. Update color values in the Python script for visualization-specific styling

### Updating Report Content

1. Edit the Markdown files in the `reports` directory
2. If you want to display the reports on the web page, convert them to HTML and add them to the appropriate sections in `web/index.html`

## Troubleshooting

### Visualization Generation Issues

- **Error: Module not found**: Ensure you've installed all dependencies with `pip install -r visualization/requirements.txt`
- **Matplotlib configuration warnings**: These can typically be ignored as they don't affect the output
- **Memory errors**: Reduce the resolution or frame count in the Python script if you encounter memory issues

### Web Display Issues

- **Images not loading**: Check file paths in HTML and ensure visualization files are in the correct directory
- **Tab switching not working**: Verify that JavaScript is enabled and the visualization-loader.js file is correctly linked
- **Styling issues**: Check for CSS conflicts with your existing website styling

## Additional Resources

- See `docs/upgrade.md` for detailed implementation instructions
- Refer to the reports in the `reports` directory for comprehensive positioning insights
- Check the comments in the Python script for detailed explanations of the visualization parameters

## Support

For additional support or to request custom modifications, please open an issue on GitHub or contact Troy Assoignon at [contact@troyassoignon.com](mailto:contact@troyassoignon.com).

---

© 2025 Troy Assoignon | Positioning Expert
