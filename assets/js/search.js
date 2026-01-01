/**
 * HI Spatial - Client-side Search (Enhanced)
 * Searches through posts using JSON index
 */

(function () {
    'use strict';

    let searchIndex = [];
    let searchInput = document.getElementById('search-input');
    let searchResults = document.getElementById('search-results');
    let searchResultsPage = document.getElementById('search-results-page');
    let searchStats = document.getElementById('search-stats');

    // Load search index
    async function loadSearchIndex() {
        try {
            const response = await fetch('/search.json');
            searchIndex = await response.json();
        } catch (error) {
            console.error('Error loading search index:', error);
        }
    }

    // Perform search
    function performSearch(query) {
        if (!query || query.length < 2) {
            return [];
        }

        const searchTerms = query.toLowerCase().split(' ').filter(term => term.length > 0);

        const results = searchIndex.filter(post => {
            const searchableText = (
                post.title + ' ' +
                post.description + ' ' +
                post.categories.join(' ') + ' ' +
                post.content
            ).toLowerCase();

            return searchTerms.every(term => searchableText.includes(term));
        });

        // Sort by relevance (title matches first)
        results.sort((a, b) => {
            const aTitle = a.title.toLowerCase();
            const bTitle = b.title.toLowerCase();
            const aHasTitleMatch = searchTerms.some(term => aTitle.includes(term));
            const bHasTitleMatch = searchTerms.some(term => bTitle.includes(term));

            if (aHasTitleMatch && !bHasTitleMatch) return -1;
            if (!aHasTitleMatch && bHasTitleMatch) return 1;
            return 0;
        });

        return results;
    }

    // Render search results for dropdown (homepage)
    function renderDropdownResults(results, container) {
        if (!container) return;

        if (results.length === 0) {
            container.innerHTML = '<p class="search-no-results">Tidak ada hasil ditemukan.</p>';
            return;
        }

        const html = results.map(post => `
      <a href="${post.url}" class="search-result-item">
        <div class="search-result-title">${post.title}</div>
        <div class="search-result-excerpt">${post.description}</div>
      </a>
    `).join('');

        container.innerHTML = html;
    }

    // Render search results for page (enhanced cards)
    function renderPageResults(results, container, query) {
        if (!container) return;

        // Update stats
        if (searchStats) {
            if (query && query.length >= 2) {
                searchStats.innerHTML = `Ditemukan <strong>${results.length}</strong> artikel untuk "<strong>${escapeHtml(query)}</strong>"`;
            } else {
                searchStats.innerHTML = '';
            }
        }

        if (results.length === 0 && query && query.length >= 2) {
            container.innerHTML = `
        <div class="search-no-results-message">
          <div class="no-results-icon">🔍</div>
          <p>Tidak ada artikel ditemukan untuk "<strong>${escapeHtml(query)}</strong>"</p>
          <p class="suggestion">Coba gunakan kata kunci yang berbeda atau lebih umum</p>
        </div>
      `;
            return;
        }

        if (!query || query.length < 2) {
            container.innerHTML = `
        <div class="search-placeholder">
          <div class="placeholder-icon">📚</div>
          <p>Ketik kata kunci untuk mencari artikel...</p>
          <p class="placeholder-hint">Minimal 2 karakter</p>
        </div>
      `;
            return;
        }

        const html = results.map(post => `
      <a href="${post.url}" class="search-result-card">
        <div class="result-date">${post.date}</div>
        <div class="result-title">${highlightMatch(post.title, query)}</div>
        <div class="result-excerpt">${post.description}</div>
        <div class="result-categories">
          ${post.categories.map(cat => `<span class="category-badge">${cat}</span>`).join('')}
        </div>
      </a>
    `).join('');

        container.innerHTML = html;
    }

    // Highlight matching text
    function highlightMatch(text, query) {
        if (!query) return text;
        const terms = query.toLowerCase().split(' ').filter(t => t.length > 0);
        let result = text;

        terms.forEach(term => {
            const regex = new RegExp(`(${escapeRegex(term)})`, 'gi');
            result = result.replace(regex, '<mark>$1</mark>');
        });

        return result;
    }

    // Escape HTML
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Escape regex special characters
    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    // Initialize search functionality
    function initSearch() {
        if (!searchInput) return;

        loadSearchIndex();

        // Debounce function
        let debounceTimer;
        function debounce(func, delay) {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(func, delay);
        }

        searchInput.addEventListener('input', function (e) {
            const query = e.target.value.trim();

            debounce(() => {
                const results = performSearch(query);

                // For dropdown results on homepage
                if (searchResults) {
                    if (query.length >= 2) {
                        searchResults.classList.add('active');
                        renderDropdownResults(results.slice(0, 5), searchResults);
                    } else {
                        searchResults.classList.remove('active');
                        searchResults.innerHTML = '';
                    }
                }

                // For search page results
                if (searchResultsPage) {
                    renderPageResults(results, searchResultsPage, query);
                }
            }, 150);
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function (e) {
            if (searchResults && !e.target.closest('.search-box') && !e.target.closest('.search-box-large')) {
                searchResults.classList.remove('active');
            }
        });

        // Handle keyboard navigation
        searchInput.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                if (searchResults) {
                    searchResults.classList.remove('active');
                }
                this.blur();
            }
        });
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSearch);
    } else {
        initSearch();
    }
})();
