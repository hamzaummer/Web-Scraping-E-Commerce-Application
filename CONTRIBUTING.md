# Contributing to Web Scraping Ecom App

Thank you for your interest in contributing to the Web Scraping Ecom App! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

1. **Check existing issues** first to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Provide detailed information**:
   - Python version
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages and stack traces

### Suggesting Features

1. **Check existing feature requests** to avoid duplicates
2. **Describe the feature** clearly and concisely
3. **Explain the use case** and why it would be valuable
4. **Consider implementation complexity** and compatibility

### Code Contributions

#### Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/web-scraping-ecom-app.git
   cd web-scraping-ecom-app
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Commit your changes**:
   ```bash
   git commit -m "Add: brief description of your changes"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**

## 📝 Coding Standards

### Python Code Style

- Follow **PEP 8** style guidelines
- Use **meaningful variable and function names**
- Add **docstrings** to all functions and classes
- Keep **line length under 88 characters**
- Use **type hints** where appropriate

### Code Organization

- **Separate concerns**: Keep scraping, database, and visualization logic separate
- **Error handling**: Always include appropriate try-catch blocks
- **Logging**: Use proper logging instead of print statements for debugging
- **Comments**: Explain complex logic and business rules

### Testing

- **Test your changes** before submitting
- **Add tests** for new functionality
- **Ensure existing tests pass**
- **Test with different websites** when modifying scraping logic

## 🔧 Development Guidelines

### Adding New CSS Selectors

When adding support for new e-commerce sites:

1. **Research the site structure** thoroughly
2. **Add selectors to the existing list** rather than replacing
3. **Test with multiple product pages**
4. **Document any site-specific quirks**

### Database Changes

- **Always provide migration scripts** for schema changes
- **Maintain backward compatibility** when possible
- **Test with existing data**

### UI/UX Changes

- **Maintain responsive design**
- **Test on different screen sizes**
- **Follow existing design patterns**
- **Ensure accessibility standards**

## 🚀 Release Process

1. **Version numbering**: Follow semantic versioning (MAJOR.MINOR.PATCH)
2. **Changelog**: Update CHANGELOG.md with new features and fixes
3. **Testing**: Ensure all tests pass and manual testing is complete
4. **Documentation**: Update README.md and other docs as needed

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Self-review of the code completed
- [ ] Comments added to hard-to-understand areas
- [ ] Documentation updated if needed
- [ ] Tests added for new functionality
- [ ] All tests pass locally

### Pull Request Description

Include:
- **Summary** of changes made
- **Motivation** for the changes
- **Testing** performed
- **Screenshots** for UI changes
- **Breaking changes** if any

## 🛡️ Legal Considerations

### Web Scraping Ethics

Contributors must ensure their changes:
- **Respect robots.txt** files
- **Include appropriate rate limiting**
- **Don't bypass anti-bot measures**
- **Follow ethical scraping practices**

### Licensing

- All contributions will be licensed under the MIT License
- Ensure you have the right to contribute the code
- Don't include copyrighted material without permission

## 🆘 Getting Help

If you need help with contributing:

1. **Check the documentation** first
2. **Search existing issues** for similar questions
3. **Join the discussion** in existing issues
4. **Create a new issue** with the "question" label

## 🙏 Recognition

Contributors will be recognized in:
- **README.md** acknowledgments section
- **CHANGELOG.md** for significant contributions
- **GitHub contributors** page

Thank you for helping make this project better! 🎉
