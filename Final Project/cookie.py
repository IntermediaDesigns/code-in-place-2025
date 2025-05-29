import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

# Global game state variables
money = 0
click_value = 1
auto_income = 0

# Global UI variables
root = None
money_label = None
income_label = None
click_value_label = None
click_button = None
upgrade_buttons = {}
cookie_image = None

# Global upgrade data
upgrades = {
    "cursor": {"cost": 15, "owned": 0, "income": 0.1, "name": "Cursor"},
    "grandma": {"cost": 100, "owned": 0, "income": 1, "name": "Grandma"},
    "farm": {"cost": 1100, "owned": 0, "income": 8, "name": "Farm"},
    "mine": {"cost": 12000, "owned": 0, "income": 47, "name": "Mine"},
    "factory": {"cost": 130000, "owned": 0, "income": 260, "name": "Factory"},
}


def load_cookie_image():
    """Load cookie image from local file or URL"""
    global cookie_image
    try:
        # First, try to load local file
        if os.path.exists("cookie.png"):
            image = Image.open("cookie.png")
        else:
            # If no local file, download from URL
            cookie_url = "https://cdn-icons-png.flaticon.com/512/541/541732.png"
            response = requests.get(cookie_url)
            image = Image.open(BytesIO(response.content))

        # Create different sized images
        button_image = image.resize((80, 80), Image.Resampling.LANCZOS)
        title_image = image.resize((30, 30), Image.Resampling.LANCZOS)

        cookie_image = {
            "button": ImageTk.PhotoImage(button_image),
            "title": ImageTk.PhotoImage(title_image),
        }
        return True

    except Exception as e:
        print(f"Could not load cookie image: {e}")
        cookie_image = None
        return False


def setup_window():
    """Initialize the main window"""
    global root
    root = tk.Tk()
    root.geometry("900x800")
    root.configure(bg="#2c3e50")
    root.resizable(True, True)
    root.minsize(800, 700)


def create_title():
    """Create the title label"""
    if cookie_image:
        title_label = tk.Label(
            root,
            text=" Cookie Clicker",
            image=cookie_image["title"],
            compound="left",
            font=("Arial", 24, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50",
        )
    else:
        title_label = tk.Label(
            root,
            text="🍪 Cookie Clicker",
            font=("Arial", 24, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50",
        )
    title_label.pack(pady=10)


def create_money_display():
    """Create money and income display labels"""
    global money_label, income_label, click_value_label

    money_label = tk.Label(
        root, text="$0", font=("Arial", 20, "bold"), fg="#f39c12", bg="#2c3e50"
    )
    money_label.pack(pady=5)

    income_label = tk.Label(
        root, text="per second: $0.0", font=("Arial", 12), fg="#95a5a6", bg="#2c3e50"
    )
    income_label.pack(pady=2)


def create_click_button():
    """Create the main cookie click button"""
    global click_button, click_value_label

    if cookie_image:
        click_button = tk.Button(
            root,
            image=cookie_image["button"],
            compound="top",
            text="CLICK ME!",
            font=("Arial", 14, "bold"),
            width=120,
            height=120,
            bg="#e67e22",
            fg="white",
            activebackground="#d35400",
            activeforeground="white",
            relief="raised",
            borderwidth=3,
            cursor="hand2",
            command=click_cookie,
        )
    else:
        click_button = tk.Button(
            root,
            text="🍪\nCLICK ME!",
            font=("Arial", 16, "bold"),
            width=15,
            height=4,
            bg="#e67e22",
            fg="white",
            activebackground="#d35400",
            activeforeground="white",
            relief="raised",
            borderwidth=3,
            cursor="hand2",
            command=click_cookie,
        )

    click_button.pack(pady=20)

    click_value_label = tk.Label(
        root, text="per click: $1", font=("Arial", 10), fg="#95a5a6", bg="#2c3e50"
    )
    click_value_label.pack()


def create_upgrades_section():
    """Create the upgrades section"""
    global upgrade_buttons

    upgrades_frame = tk.Frame(root, bg="#34495e")
    upgrades_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Upgrades title
    if cookie_image:
        upgrades_title = tk.Label(
            upgrades_frame,
            text=" UPGRADES",
            image=cookie_image["title"],
            compound="left",
            font=("Arial", 14, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
        )
    else:
        upgrades_title = tk.Label(
            upgrades_frame,
            text="🛒 UPGRADES",
            font=("Arial", 14, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
        )
    upgrades_title.pack(pady=5)

    # Create upgrade buttons
    for upgrade_id, upgrade_data in upgrades.items():
        frame = tk.Frame(upgrades_frame, bg="#34495e")
        frame.pack(fill="x", pady=2)

        button = tk.Button(
            frame,
            text=f"{upgrade_data['name']} - ${upgrade_data['cost']:,}",
            font=("Arial", 10, "bold"),
            width=25,
            height=2,
            bg="#27ae60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            relief="raised",
            borderwidth=2,
            cursor="hand2",
            command=lambda uid=upgrade_id: buy_upgrade(uid),
        )
        button.pack(side="left", padx=5)

        info_label = tk.Label(
            frame,
            text=f"Owned: 0 | +${upgrade_data['income']}/sec",
            font=("Arial", 9),
            fg="#bdc3c7",
            bg="#34495e",
        )
        info_label.pack(side="left", padx=10)

        upgrade_buttons[upgrade_id] = {"button": button, "info": info_label}


def click_cookie():
    """Handle cookie click"""
    global money, click_value
    money += click_value
    update_displays()

    # Visual feedback
    click_button.configure(relief="sunken")
    root.after(50, lambda: click_button.configure(relief="raised"))


def buy_upgrade(upgrade_id):
    """Handle upgrade purchase"""
    global money, auto_income, click_value
    upgrade = upgrades[upgrade_id]

    if money >= upgrade["cost"]:
        money -= upgrade["cost"]
        upgrade["owned"] += 1
        auto_income += upgrade["income"]

        # Increase cost for next purchase (15% increase)
        upgrade["cost"] = int(upgrade["cost"] * 1.15)

        # Special bonuses
        if upgrade_id == "cursor" and upgrade["owned"] % 5 == 0:
            click_value += 1

        update_displays()


def auto_generate():
    """Generate automatic income"""
    global money, auto_income
    if auto_income > 0:
        money += auto_income / 10  # Called every 100ms, so divide by 10

    update_displays()
    root.after(100, auto_generate)  # Update every 100ms


def update_displays():
    """Update all display elements"""
    global money, auto_income, click_value

    # Update money display
    if money >= 1000000:
        money_text = f"${money/1000000:.1f}M"
    elif money >= 1000:
        money_text = f"${money/1000:.1f}K"
    else:
        money_text = f"${money:.0f}"

    money_label.config(text=money_text)
    income_label.config(text=f"per second: ${auto_income:.1f}")
    click_value_label.config(text=f"per click: ${click_value}")

    # Update upgrade buttons
    for upgrade_id, upgrade_data in upgrades.items():
        button_info = upgrade_buttons[upgrade_id]

        # Update button text and color
        button_text = f"{upgrade_data['name']} - ${upgrade_data['cost']:,}"
        button_info["button"].config(text=button_text)

        # Change color and cursor based on affordability
        if money >= upgrade_data["cost"]:
            button_info["button"].config(
                bg="#27ae60",
                fg="white",
                activebackground="#229954",
                activeforeground="white",
                cursor="hand2",
                state="normal",
            )
        else:
            button_info["button"].config(
                bg="#7f8c8d",
                fg="white",
                activebackground="#6c7b7d",
                activeforeground="white",
                cursor="X_cursor",
                state="normal",
            )

        # Update info text
        total_income = upgrade_data["income"] * upgrade_data["owned"]
        info_text = f"Owned: {upgrade_data['owned']} | +${total_income:.1f}/sec"
        button_info["info"].config(text=info_text)


def setup_ui():
    """Initialize all UI elements"""
    load_cookie_image()
    create_title()
    create_money_display()
    create_click_button()
    create_upgrades_section()


def run_game():
    """Main game loop"""
    setup_window()
    setup_ui()
    update_displays()
    auto_generate()
    root.mainloop()


# Run the game
if __name__ == "__main__":
    run_game()
