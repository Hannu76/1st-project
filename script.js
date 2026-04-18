// Liquid Glass Header Effect
        window.addEventListener('scroll', () => {
            const header = document.getElementById('header');
            if (window.scrollY > 50) header.classList.add('scrolled');
            else header.classList.remove('scrolled');
        });

        // Mobile Menu
        const mobileToggle = document.getElementById('mobileToggle');
        const navMenu = document.getElementById('navMenu');
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        // Scroll Reveal Array
        const reveals = document.querySelectorAll('.reveal-text, .reveal-left, .reveal-right, .reveal-up, .reveal-pop, .reveal-zoom-out');
        const revealOnScroll = () => {
            let windowHeight = window.innerHeight;
            reveals.forEach(reveal => {
                let elementTop = reveal.getBoundingClientRect().top;
                if (elementTop < windowHeight - 100) reveal.classList.add('active');
            });
        };
        revealOnScroll();
        window.addEventListener('scroll', revealOnScroll);

        // Booking Logic via WhatsApp
        function submitBooking() {
            const name = document.getElementById('bookName').value.trim();
            const date = document.getElementById('bookDate').value;
            let time = document.getElementById('bookTime').value;
            
            if(!name || !date || !time) {
                alert("Please fill all details (Name, Date, Time) to book your appointment.");
                return;
            }
            
            const timeParts = time.split(':');
            let hour = parseInt(timeParts[0]);
            const min = timeParts[1];
            const ampm = hour >= 12 ? 'PM' : 'AM';
            hour = hour % 12;
            hour = hour ? hour : 12;
            const formattedTime = hour + ':' + min + ' ' + ampm;
            
            const dateObj = new Date(date);
            const formattedDate = dateObj.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });

            const message = `Hello Sun Shine Dental Clinic! I would like to confirm my appointment.%0A%0A*Name:* ${name}%0A*Date:* ${formattedDate}%0A*Time:* ${formattedTime}`;
            const whatsappUrl = `https://wa.me/919553898583?text=${message}`;
            window.open(whatsappUrl, '_blank');
        }
