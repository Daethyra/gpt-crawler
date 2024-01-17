import { Config } from "./src/config";

export const defaultConfig: Config = {
  url: "https://python.langchain.com/docs/get_started/introduction",
  match: [
    "https://python.langchain.com/docs/**",
  ],
    maxPagesToCrawl: 15,
  outputFileName: "output.json",
};
