const js = {
  rules: {
    "no-unused-vars": "warn",
    "no-undef": "error"
  }
};

module.exports = [
  {
    languageOptions: {
      ecmaVersion: 2021,
      globals: {
        require: "readonly",
        process: "readonly",
        console: "readonly",
        __dirname: "readonly",
        module: "readonly"
      }
    },
    rules: js.rules
  }
];