class HardwareDatabase:
    """Manages the silicon dataset using pure Python dictionaries and lists."""
    
    def __init__(self):
        #  [DATA INTERFACE] Comprehensive list of 20 real AMD processors
        self.raw_data = [
            # --- The Modern Era: Zen 5 & Zen 4 ---
            {"Processor": "Ryzen 9 9950X", "Generation": "Zen 5", "Price": 649, "Performance": 100, "Demand": 85},
            {"Processor": "Ryzen 9 9900X", "Generation": "Zen 5", "Price": 499, "Performance": 92, "Demand": 75},
            {"Processor": "Ryzen 7 9700X", "Generation": "Zen 5", "Price": 359, "Performance": 85, "Demand": 80},
            {"Processor": "Ryzen 5 9600X", "Generation": "Zen 5", "Price": 279, "Performance": 72, "Demand": 85},
            {"Processor": "Ryzen 7 7800X3D", "Generation": "Zen 4", "Price": 399, "Performance": 98, "Demand": 100},
            {"Processor": "Ryzen 9 7950X", "Generation": "Zen 4", "Price": 549, "Performance": 96, "Demand": 80},
            {"Processor": "Ryzen 5 7600X", "Generation": "Zen 4", "Price": 229, "Performance": 75, "Demand": 90},
            
            # --- The Value Champions: Zen 3 & Zen 2 ---
            {"Processor": "Ryzen 7 5800X3D", "Generation": "Zen 3", "Price": 320, "Performance": 80, "Demand": 95},
            {"Processor": "Ryzen 9 5900X", "Generation": "Zen 3", "Price": 349, "Performance": 84, "Demand": 75},
            {"Processor": "Ryzen 5 5600X", "Generation": "Zen 3", "Price": 150, "Performance": 60, "Demand": 90},
            {"Processor": "Ryzen 7 3700X", "Generation": "Zen 2", "Price": 130, "Performance": 50, "Demand": 65},
            {"Processor": "Ryzen 5 3600", "Generation": "Zen 2", "Price": 95, "Performance": 45, "Demand": 85},
            
            # --- The Pioneers: Zen 1 & Zen+ ---
            {"Processor": "Ryzen 7 2700X", "Generation": "Zen+", "Price": 90, "Performance": 38, "Demand": 40},
            {"Processor": "Ryzen 5 2600", "Generation": "Zen+", "Price": 75, "Performance": 32, "Demand": 50},
            {"Processor": "Ryzen 7 1700X", "Generation": "Zen 1", "Price": 85, "Performance": 30, "Demand": 30},
            {"Processor": "Ryzen 5 1600", "Generation": "Zen 1", "Price": 60, "Performance": 25, "Demand": 45},
            
            # --- Classic Tech & Historical Chips ---
            {"Processor": "AMD FX-8350", "Generation": "Bulldozer", "Price": 70, "Performance": 18, "Demand": 15},
            {"Processor": "AMD FX-6300", "Generation": "Bulldozer", "Price": 50, "Performance": 12, "Demand": 10},
            {"Processor": "Phenom II X6 1090T", "Generation": "Classic Tech", "Price": 55, "Performance": 14, "Demand": 8},
            {"Processor": "Athlon 64 X2 6000+", "Generation": "Classic Tech", "Price": 25, "Performance": 4, "Demand": 2}
        ]
        #  [DATA INTERFACE] Compute Value Scores directly using a pure loop at startup
        for cpu in self.raw_data:
            cpu["Value Score"] = round((cpu["Performance"] / cpu["Price"]) * 100, 1)

    def get_unique_generations(self) -> list:
        #  [DATA INTERFACE] Extract unique category labels cleanly without duplicates
        generations = set(cpu["Generation"] for cpu in self.raw_data)
        return sorted(list(generations))

    def filter_and_rank(self, generations: list, max_budget: int) -> list:
        if not generations:
            return []

        filtered_list = []
        for cpu in self.raw_data:
            if cpu["Generation"] in generations and cpu["Price"] <= max_budget:
                filtered_list.append(cpu)

        return sorted(filtered_list, key=lambda x: x["Value Score"], reverse=True)             