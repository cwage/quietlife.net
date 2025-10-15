# Changelog

## 2024-12-26

### Changed
- **Replaced kramdown with CommonMark** to avoid direct rexml dependency
  - Added `jekyll-commonmark` plugin for Jekyll integration  
  - Added `commonmarker` gem for CommonMark implementation
  - Configured CommonMark with SMART quotes, footnotes, strikethrough, autolink, and table extensions
  - All existing markdown content continues to render correctly
  - While Jekyll itself still has kramdown as a dependency, the site's markdown content is now processed entirely by CommonMark
  - This change reduces the direct dependency on rexml for markdown processing, addressing security concerns