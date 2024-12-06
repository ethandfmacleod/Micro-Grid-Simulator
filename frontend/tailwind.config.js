/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: ["class"],
    content: ["./index.html", "./src/**/*.{ts,tsx,js,jsx}"],
  theme: {
  	extend: {
  		borderRadius: {
  			lg: 'var(--radius)',
  			md: 'calc(var(--radius) - 2px)',
  			sm: 'calc(var(--radius) - 4px)'
  		},
  		colors: {
			primary: "hsl(var(--primary))",
			"primary-foreground": "hsl(var(--primary-foreground))",
			secondary: "hsl(var(--secondary))",
			"secondary-foreground": "hsl(var(--secondary-foreground))",
			muted: "hsl(var(--muted))",
			"muted-foreground": "hsl(var(--muted-foreground))",
			accent: "hsl(var(--accent))",
			"accent-foreground": "hsl(var(--accent-foreground))",
			destructive: "hsl(var(--destructive))",
			"destructive-foreground": "hsl(var(--destructive-foreground))",
			background: "hsl(var(--background))",
			foreground: "hsl(var(--foreground))",
			card: "hsl(var(--card))",
			"card-foreground": "hsl(var(--card-foreground))",
			popover: "hsl(var(--popover))",
			"popover-foreground": "hsl(var(--popover-foreground))",
		},
		borderRadius: {
		DEFAULT: "var(--radius)",
		},
  	}
  },
  plugins: [require("tailwindcss-animate")],
}