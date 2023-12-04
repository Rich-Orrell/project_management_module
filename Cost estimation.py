class computerBuilder:
    def __init__(self, specs, costs, dev_time, os, os_dev_time):
        self.specs = specs
        self.costs = costs
        self.dev_time = dev_time
        self.os = os
        self.os_dev_time = os_dev_time


    def generate_cost_estimate(self):
        cost_estimate = self.calc_cost(computer_specs)
        dev_time_estimate = self.calc_dev_time(computer_specs)
        os_dev_time_estimate = self.calc_os_dev_time(software_choice['OS'])

        return { # Returns values to be used in menu option 1.
            'selected_specs': computer_specs,
            'cost_estimate': cost_estimate,
            'dev_time_estimate': dev_time_estimate,
            'os_dev_time_estimate': os_dev_time_estimate
        }

    def choose_specs(self):
        
        print("\nWhich component would you like to update?") # User selects which component to select.
        for key in self.specs.keys():
            print(key)
        selected_key = input()
        if selected_key in self.specs:
            print("\nSelect which", selected_key,  "part you would like to use:") # User selects the model of the component to use.
            for val in self.specs[selected_key]:
                print(val)
            selected_val = input()
            if selected_val in self.specs[selected_key]:
                print("\nThank you. This part has been added to the specs.")
                if selected_key == 'IOP': # Multiple IOP parts can be used. All other parts will be replaced by new choice.
                    computer_specs[selected_key].append(selected_val)
                else:
                    computer_specs[selected_key] = selected_val
            else:
                print("\nI'm sorry, that part is not on the list. Please try again.")
        else:
            print("\nI'm sorry, that is not a valid part. Please try again.")

    def choose_OS(self):
        
        print("\nWhich OS would you like to use?")
        for key in self.os:
            print(key)
        selected_key = input()
        if selected_key in self.os:
            software_choice['OS'] = selected_key
        else:
            print("\nI'm sorry, that is not a valid OS. Please try again.")

    def calc_cost(self, selected_specs):
        total_cost = 0
        for category in selected_specs:
            if isinstance(selected_specs[category], list):
                for i in selected_specs[category]:
                    total_cost += self.costs[category][i]
            else:
                total_cost += self.costs[category][selected_specs[category]]
        return total_cost

    def calc_dev_time(self, selected_specs):
        total_cost = 0
        for category in selected_specs:
            if isinstance(selected_specs[category], list):
                for i in selected_specs[category]:
                    total_cost += self.dev_time[category][i]
            else:
                total_cost += self.dev_time[category][selected_specs[category]]
        return total_cost
    
    def calc_os_dev_time(self, selected_os):
        total_time = sum(self.os_dev_time[selected_os][category] for category in os_dev_time[selected_os])
        return total_time

opt_specs = { # Specs based on appendix 1 spreadsheet.
    'CPU': ['68k0', '68k8', 'EP7500FE'],
    'RAM': ['32KB', '128KB', '256KB', '512KB', 'SIMM 1024KB', 'SIMM 2048KB', 'SIMM 4096KB'], 
    'ROM': ['8KB', '16KB', '32KB'],
    'ULA': ['G1', 'G2', 'G3', 'G4', 'GX', 'DAC'],
    'Storage': ['Disk', 'Cartridge', 'Mixed'],
    'Case': ['Desktop', 'Luggable'], 
    'IOP': ['16550 UART', 'J6100', 'SC100', 'SC150', 'SCSI']
}

opt_cost = { # Costs based on appendix 1 spreadsheet.
    'CPU': {'68k0': 8, '68k8': 5.5, 'EP7500FE': 15},
    'RAM': {'32KB': 1.5, '128KB': 2.5, '256KB': 5, '512KB': 10, 'SIMM 1024KB': 15, 'SIMM 2048KB': 25, 'SIMM 4096KB': 60}, 
    'ROM': {'8KB': 1.5, '16KB': 2, '32KB': 4}, 
    'ULA': {'G1': 5, 'G2': 5, 'G3': 5, 'G4': 5, 'GX': 5, 'DAC': 5},
    'Storage': {'Disk': 7.5, 'Cartridge': 5, 'Mixed': 12.5},
    'Case': {'Desktop': 25, 'Luggable': 35},
    'IOP': {'16550 UART': 5, 'J6100': 5, 'SC100': 12, 'SC150': 15, 'SCSI': 5}
}

opt_dev_time = { # Development time based on appendix 1 spreadsheet # Time is in weeks.
    'CPU': {'68k0': 0, '68k8': 0, 'EP7500FE': 0},
    'RAM': {'32KB': 0, '128KB': 0, '256KB': 0, '512KB':0, 'SIMM 1024KB': 0, 'SIMM 2048KB': 0, 'SIMM 4096KB': 0},
    'ROM': {'8KB': 4, '16KB': 4, '32KB': 4},
    'ULA': {'G1': 4, 'G2': 4, 'G3': 4, 'G4': 4, 'GX': 5, 'DAC': 4},
    'Storage': {'Disk': 10, 'Cartridge': 10, 'Mixed': 20},
    'Case': {'Desktop': 10, 'Luggable': 10},
    'IOP': {'16550 UART': 0, 'J6100': 0, 'SC100': 0, 'SC150': 0, 'SCSI': 0}
}

software_os = [ # Operating systems based on appendix 2 spreadsheet.
    'HB/OS',
    'MCC OS'
]

os_dev_time = { # Development time based on appendix 2 spreadsheet.
    'HB/OS': {'Kernel': 8, 'Libraries': 0, 'Drivers': 0, 'Extensions': 2, 'GameSnd': 2, 'Graphics': 4},
    'MCC OS': {'Kernel': 6, 'Libraries': 0, 'Drivers': 0, 'Extensions': 4, 'GameSnd': 4, 'Graphics': 3}
}

computer_specs = { # Specifications chosen by user in the UI will populate this table.
    'CPU': [],
    'RAM': [],
    'ROM': [],
    'ULA': [],
    'Storage': [],
    'Case': [],
    'IOP': []
}

software_choice = { # Operating system chosen by user in the UI will populate this table.
    'OS': []
}

computer_builder = computerBuilder(opt_specs, opt_cost, opt_dev_time, software_os, os_dev_time)

opt_menu = -1

while opt_menu != 0: # Main menu.
    print("")
    print("Welcome to Cost Estimation for a 1980s computer")
    print("Current computer specs:", computer_specs)
    print("Current computer operating system:", software_choice['OS'])
    print("Please select an option from the menu below")
    print("1. See details for existing computer specs.")
    print("2. Update hardware requirements.")
    print("3. Update software requirements")
    print("0. Exit")
    opt_menu = int(input())

    if opt_menu == 1: # Option 1 - See cost and development time details for computer based on chosen specifications.
        if any(not computer_specs[key] for key in computer_specs) or any(not software_choice[key] for key in software_choice):
            print("\nPlease select a spec for each component and the operating system before generating details.")
        else:
            cost_estimate = computer_builder.generate_cost_estimate()
            dev_cost = 40*(cost_estimate['dev_time_estimate'])
            os_dev_cost = 40*(cost_estimate['os_dev_time_estimate'])
            total_cost = ((1000 * (cost_estimate['cost_estimate'] + 0.5 * 100)) + dev_cost + os_dev_cost) / 1000 # Added chosen OS dev costs, hardware related costs, additional required misc costs from appendix 1. Dev costs split over cost of 1000 orders.
            print("\nSelected Specs:", cost_estimate['selected_specs'])
            print("Cost of parts: £", cost_estimate['cost_estimate']  + (0.5 * 100)) # Required misc parts from appendix 1 added onto cost.
            print("Development time:", cost_estimate['dev_time_estimate'], " weeks")
            print("Development cost: £", dev_cost)
            print("Software development time:", cost_estimate['os_dev_time_estimate'], 'weeks.')
            print("Sofware development cost: £", os_dev_cost)
            print("Total cost: £", total_cost)
            print("Price to customers: £", 1.25 * total_cost) # Markup price to customers of 25% added on.
            input()
    
    if opt_menu == 2: # Option 2 - Select computer hardware.
        computer_builder.choose_specs()
        
    if opt_menu == 3: # Option 3 - Select operating system.
        computer_builder.choose_OS()

    if opt_menu == 0: # Option 4 - Exit software.
        print("Thank you, goodbye.")
        break