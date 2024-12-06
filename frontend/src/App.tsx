import { Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage/HomePage";
import { ThemeProvider } from "./components/ui/ThemeProvider";
import { Provider } from "react-redux";
import { store } from "./store/store";

function App() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
        <Provider store={store}>
            <Routes>
                <Route path="/" element={<HomePage />} />
                {/* <Route path="/project/:flowsheetId/">
                    <Route path="flowsheet" element={<FlowsheetPage />} />
                </Route> */}
            </Routes>
        </Provider>
    </ThemeProvider>
  )
}

export default App
