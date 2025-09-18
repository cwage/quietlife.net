# Changelog

## 2024-12-26

### Changed
- **Replaced kramdown with CommonMark** to avoid direct rexml dependency
  - Added `jekyll-commonmark` plugin for Jekyll integration  
  - Added `commonmarker` gem for CommonMark implementation
  - Configured CommonMark with SMART quotes, footnotes, strikethrough, autolink, and table extensions
  - Verified that Jekyll is correctly using CommonMark for all markdown content processing
  - Updated all dependencies to latest compatible versions
  - All existing markdown content continues to render correctly
  - While Jekyll core still has kramdown as a transitive dependency (required for backward compatibility), the site's markdown content is now processed entirely by CommonMark
  - This change eliminates direct usage of rexml for markdown processing, significantly reducing security exposure