/**
 * Mermaid.js Configuration for EKGF Custom Colors
 * 
 * IMPORTANT: 
 * - We use Material for MkDocs' NATIVE Mermaid support (NOT mkdocs-mermaid2-plugin!)
 * - Do NOT install mkdocs-mermaid2-plugin - it conflicts with Material's native support
 * - Material for MkDocs automatically looks for window.mermaidConfig in extra_javascript files
 * - This configuration applies to all Mermaid diagrams site-wide
 * 
 * Color Scheme (EKGF Brand):
 * - Primary: #4051b5 (Indigo blue) - node backgrounds
 * - Accent: #ff6f00 (EKGF orange) - borders and connector lines
 * - Text: #ffffff (White) - for contrast on colored nodes
 * 
 * How It Works:
 * 1. Material for MkDocs reads window.mermaidConfig before initializing Mermaid
 * 2. This file is loaded via extra_javascript in mkdocs.yml
 * 3. The theme variables override Material's defaults
 * 4. No need for inline %%{init}%% directives in diagrams
 */

window.mermaidConfig = {
  theme: 'base',
  themeVariables: {
    primaryColor: '#4051b5',
    primaryTextColor: '#ffffff',
    primaryBorderColor: '#ff6f00',
    lineColor: '#ff6f00',
    secondaryColor: '#4051b5',
    secondaryTextColor: '#ffffff',
    secondaryBorderColor: '#ff6f00',
    tertiaryColor: '#4051b5',
    tertiaryTextColor: '#ffffff',
    tertiaryBorderColor: '#ff6f00',
    background: '#ffffff',
    mainBkg: '#4051b5',
    secondaryBkg: '#4051b5',
    tertiaryBkg: '#4051b5',
    textColor: '#ffffff',
    nodeBorder: '#ff6f00',
    clusterBkg: '#4051b5',
    clusterBorder: '#ff6f00',
    defaultLinkColor: '#ff6f00',
    titleColor: '#333333',
    edgeLabelBackground: '#ffffff'
  }
};

