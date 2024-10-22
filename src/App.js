import { useEffect } from "react";
import buttonConfig from "./buttonConfig";

function App(){

  useEffect(() => {
    const script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/gh/VapiAI/html-script-tag@latest/dist/assets/index.js";
    script.async = true;
    document.body.appendChild(script);

    script.onload = () => {
      window.vapiSDK.run({
        apiKey: "63aeff52-a75a-47c5-94df-1dfa01942f4a",
        assistant: "47a9a5be-8db4-4683-a808-0ad9e1574a4b",
        config: buttonConfig,
      });
    };
 }, []);

}

export default App
