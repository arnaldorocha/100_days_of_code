    let currentLang = 'en';

    function toggleLanguage() {
      const allLangElements = document.querySelectorAll('.lang');
      allLangElements.forEach(el => el.classList.remove('visible'));

      currentLang = currentLang === 'en' ? 'pt' : 'en';

      const visibleLangs = document.querySelectorAll(`.lang.${currentLang}`);
      visibleLangs.forEach(el => el.classList.add('visible'));
    }
