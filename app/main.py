"""
Hello World Landing Page - Professional Implementation
A modern, responsive landing page built with NiceGUI
"""
from nicegui import ui
import random
from app.core.assets import ProfessionalAssetManager

# Get professional images for our landing page
project_type = "portfolio"
hero_image = ProfessionalAssetManager.get_hero_image(project_type)
feature_images = ProfessionalAssetManager.get_project_images(project_type, count=3)

# Apply custom CSS for professional styling
with ui.head():
    ui.add_css_path('app/static/css/main.css')

@ui.page('/')
def index():
    """Main landing page"""
    with ui.column().classes('w-full max-w-screen-xl mx-auto px-4 py-8'):
        # Hero Section
        with ui.card().classes('hero-section w-full p-8 mb-12'):
            ui.image(hero_image).classes('w-full h-64 object-cover rounded-xl mb-6')
            ui.label('Hello World').classes('text-4xl font-bold mb-2')
            ui.label('Welcome to our innovative digital platform').classes('text-xl mb-6')
            with ui.row().classes('justify-center gap-4'):
                ui.button('Get Started', icon='rocket_launch').classes('btn-primary')
                ui.button('Learn More', icon='info').classes('btn-secondary')
        
        # Value Proposition
        with ui.row().classes('w-full mb-12 items-center'):
            with ui.column().classes('w-full lg:w-1/2 pr-0 lg:pr-8'):
                ui.label('Modern Solutions for Modern Problems').classes('text-2xl font-bold mb-4')
                ui.label(
                    'Our platform leverages cutting-edge technology to deliver exceptional results. '
                    'We combine innovation with reliability to ensure your success in the digital landscape.'
                ).classes('text-lg mb-4')
                ui.button('Explore Features', icon='explore').classes('btn-primary')
            
            with ui.column().classes('w-full lg:w-1/2 mt-8 lg:mt-0'):
                ui.image(feature_images[0]).classes('w-full h-64 object-cover rounded-xl shadow-lg')
        
        # Features Section
        ui.label('Our Key Features').classes('text-2xl font-bold mb-6 text-center w-full')
        
        with ui.grid(columns=3).classes('feature-grid'):
            # Feature 1
            with ui.card().classes('feature-card'):
                ui.image(feature_images[0]).classes('w-full h-40 object-cover rounded-t-xl')
                with ui.card_section():
                    ui.label('Innovative Design').classes('text-xl font-bold mb-2')
                    ui.label('Modern, responsive interfaces that adapt to any device or screen size.')
                    ui.button('Learn More', icon='arrow_forward').classes('btn-text mt-4')
            
            # Feature 2
            with ui.card().classes('feature-card'):
                ui.image(feature_images[1]).classes('w-full h-40 object-cover rounded-t-xl')
                with ui.card_section():
                    ui.label('Powerful Analytics').classes('text-xl font-bold mb-2')
                    ui.label('Gain insights with our comprehensive data visualization tools.')
                    ui.button('Learn More', icon='arrow_forward').classes('btn-text mt-4')
            
            # Feature 3
            with ui.card().classes('feature-card'):
                ui.image(feature_images[2]).classes('w-full h-40 object-cover rounded-t-xl')
                with ui.card_section():
                    ui.label('Secure Platform').classes('text-xl font-bold mb-2')
                    ui.label('Enterprise-grade security to protect your valuable data.')
                    ui.button('Learn More', icon='arrow_forward').classes('btn-text mt-4')
        
        # Testimonials
        with ui.card().classes('w-full my-12 p-8 bg-neutral-50'):
            ui.label('What Our Clients Say').classes('text-2xl font-bold mb-6 text-center')
            
            with ui.row().classes('gap-6 flex-wrap justify-center'):
                for i in range(2):
                    with ui.card().classes('testimonial-card w-full md:w-5/12'):
                        with ui.row().classes('items-center mb-4'):
                            ui.icon('format_quote', size='xl').classes('text-primary-500')
                            ui.label(['Amazing platform!', 'Exceeded our expectations!'][i]).classes('text-lg font-bold ml-2')
                        ui.label([
                            'The interface is intuitive and the features are exactly what we needed for our project.',
                            'The support team was responsive and helped us implement the solution in record time.'
                        ][i]).classes('mb-4')
                        with ui.row().classes('items-center'):
                            ui.avatar(f'https://i.pravatar.cc/150?img={random.randint(1, 70)}')
                            with ui.column().classes('ml-4'):
                                ui.label(['Sarah Johnson', 'Michael Chen'][i]).classes('font-bold')
                                ui.label(['CTO, TechCorp', 'Product Manager, InnovateCo'][i]).classes('text-sm text-neutral-500')
        
        # Call to Action
        with ui.card().classes('w-full p-8 text-center cta-section'):
            ui.label('Ready to Get Started?').classes('text-2xl font-bold mb-4')
            ui.label('Join thousands of satisfied customers using our platform today.').classes('mb-6')
            with ui.row().classes('justify-center gap-4'):
                ui.button('Sign Up Now', icon='person_add').classes('btn-primary')
                ui.button('Schedule Demo', icon='calendar_today').classes('btn-secondary')
        
        # Footer
        with ui.row().classes('w-full mt-12 pt-6 border-t border-neutral-200 justify-between items-center'):
            ui.label('© 2023 Hello World Platform. All rights reserved.').classes('text-sm text-neutral-500')
            with ui.row().classes('gap-4'):
                for icon in ['facebook', 'twitter', 'linkedin', 'github']:
                    ui.button(icon=icon, color='black').props('flat round')