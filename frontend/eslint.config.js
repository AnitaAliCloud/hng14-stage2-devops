export default [
  {
    languageOptions: {
      ecmaVersion: 2021,
      globals: {
        require: "readonly",
        process: "readonly",
        console: "readonly",
        __dirname: "readonly"
      }
    },
    rules: {
      "no-unused-vars": "warn",
      "no-undef": "error"
    }
  }
];
