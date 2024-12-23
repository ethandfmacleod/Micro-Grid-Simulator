import { Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage/HomePage";
import { ThemeProvider } from "./components/ui/ThemeProvider";
import { Provider } from "react-redux";
import { store } from "./store/store";
import { DesignPage } from "./pages/DesignPage/DesignPage";

function App() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <Provider store={store}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/project/:projectId/">
            <Route path="design" element={<DesignPage />} />
          </Route>
        </Routes>
      </Provider>
    </ThemeProvider>
  )
}

export default App
