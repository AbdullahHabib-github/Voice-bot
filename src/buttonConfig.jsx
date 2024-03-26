const buttonConfig = {
    position: "bottom-right", // "bottom" | "top" | "left" | "right" | "top-right" | "top-left" | "bottom-left" | "bottom-right"
    offset: "40px", // decide how far the button should be from the edge
    width: "50px", // min-width of the button
    height: "50px", // height of the button
    idle: { // button state when the call is not active.
      color: `rgb(93, 254, 202)`, 
      type: "pill", // or "round"
      title: "Have a quick question?", // only required in case of Pill
      subtitle: "Talk with our AI assistant", // only required in case of pill
      icon: `https://unpkg.com/lucide-static@0.321.0/icons/phone.svg`,
    },
    loading: { // button state when the call is connecting
      color: `rgb(93, 124, 202)`,
      type: "pill", // or "round"
      title: "Connecting...", // only required in case of Pill
      subtitle: "Please wait", // only required in case of pill
      icon: `https://unpkg.com/lucide-static@0.321.0/icons/loader-2.svg`,
    },
    active: { // button state when the call is in progress or active.
      color: `rgb(255, 0, 0)`,
      type: "pill", // or "round"
      title: "Call is in progress...", // only required in case of Pill
      subtitle: "End the call.", // only required in case of pill
      icon: `https://unpkg.com/lucide-static@0.321.0/icons/phone-off.svg`,
    },
  };
  

  


  export default buttonConfig