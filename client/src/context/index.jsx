import React, { createContext, useState } from "react";
export const AppContext = createContext();

export const FileContextProvider = ({ children }) => {
  // Test
  const [value, setValue] = useState(0);

  // App Data
  const [status, setStatus] = useState(0);

  return (
    <AppContext.Provider
      value={{
        value,
        setValue,
        status,
        setStatus,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
