import { Config } from "./src/config";

export const defaultConfig: Config = {
  url: "https://api.python.langchain.com/en/stable/langchain_api_reference.html",
  match: "https://api.python.langchain.com/en/stable/**",
  maxPagesToCrawl: 50,
  outputFileName: "output.json",
};
