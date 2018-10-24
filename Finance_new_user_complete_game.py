from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
import time


class FullGame:
    def new_user_full_game(self):
        baseurl = 'https://finance.hemisphereapp.io'
        driver = webdriver.Chrome()
        # options.add_argument('--disable-extensions')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--no-sandbox')
        driver.get(baseurl)
        driver.implicitly_wait(5)

        signup_click = driver.find_element_by_tag_name('a')
        signup_click.click()
        time.sleep(2)

        name_input = driver.find_element_by_id('name')
        fake_name = Faker()
        name_input.send_keys('test_' + fake_name.first_name())
        time.sleep(4)
        confirmation_name = driver.find_element_by_tag_name('a')
        confirmation_name.click()

        email_input = driver.find_element_by_id('email')
        fake_email = Faker()
        email_input.send_keys('test_rare_' + fake_email.email())
        time.sleep(2)
        confirmation_email = driver.find_element_by_xpath('/html/body/app-root/div['
                                                          '2]/div/app-signup/div/form/div/div/div/div[2]/div/div/a')
        confirmation_email.click()

        password_input = driver.find_element_by_id('password')
        password_input.send_keys('ABC123')
        time.sleep(2)
        confirmation_password = driver.find_element_by_xpath('/html/body/app-root/div['
                                                             '2]/div/app-signup/div/form/div/div/div/div['
                                                             '3]/div/div/a[1]')
        confirmation_password.click()

        password_confirm = driver.find_element_by_id('passwordConfirm')
        password_confirm.send_keys('ABC123')
        time.sleep(2)
        repeat_password = driver.find_element_by_xpath('/html/body/app-root/div['
                                                       '2]/div/app-signup/div/form/div/div/div/div[4]/div/div/a[1]')
        repeat_password.click()
        time.sleep(2)

        invitation_code = driver.find_element_by_id('invitationCode')
        invitation_code.send_keys('magic')
        submit_button = driver.find_element_by_xpath('//span[text()="Register"]')
        submit_button.click()
        time.sleep(2)

        watch_intro_video = driver.find_element_by_xpath("//span[text()='Watch now']")
        watch_intro_video.click()
        time.sleep(130)

        skip_welcome = driver.find_element_by_xpath("//a[text()='Next']")
        skip_welcome.click()
        time.sleep(4)

        bubbleone = driver.find_element_by_xpath("//*[contains(text(), 'Relevant')]")
        bubbleone.click()
        time.sleep(1)
        bubbletwo = driver.find_element_by_xpath("//*[contains(text(), 'Clear')]")
        bubbletwo.click()
        time.sleep(1)
        bubblethree = driver.find_element_by_xpath("//*[contains(text(), 'Concise')]")
        bubblethree.click()
        time.sleep(1)
        bubblefour = driver.find_element_by_xpath("//*[contains(text(), 'Succinct')]")
        bubblefour.click()
        time.sleep(1)
        bubblefive = driver.find_element_by_xpath("(//*[@class=\"node valid \"])[2]")
        bubblefive.click()
        time.sleep(1)
        bubblesix = driver.find_element_by_xpath("//*[contains(text(), 'Structured')]")
        bubblesix.click()
        time.sleep(1)
        bubbleseven = driver.find_element_by_xpath("(//*[@class=\"node valid \"])[4]")
        bubbleseven.click()
        time.sleep(1)
        bubbleeight = driver.find_element_by_xpath("//*[contains(text(), 'Relevant')]")
        bubbleeight.click()
        time.sleep(2)
        goodinterviewsubmit = driver.find_element_by_xpath("//*[contains(text(), 'SUBMIT')]")
        goodinterviewsubmit.click()
        time.sleep(4)

        bubbleone = driver.find_element_by_xpath("(//*[local-name()='circle'][@class=\"node valid \"])[9]")
        bubbleone.click()
        time.sleep(1)
        bubbletwo = driver.find_element_by_xpath("(//*[@class=\"node valid \"])[11]")
        bubbletwo.click()
        time.sleep(1)
        bubblethree = driver.find_element_by_xpath("//*[local-name()='tspan'][text()=\"candidate says over how\"]")
        bubblethree.click()
        time.sleep(1)
        bubblefour = driver.find_element_by_xpath("(//*[@class=\"node valid \"])[12]")
        bubblefour.click()
        time.sleep(1)
        bubblefive = driver.find_element_by_xpath("//*[local-name()='tspan'][text()=\"reflect before scoring\"]")
        bubblefive.click()
        time.sleep(1)
        bubblesix = driver.find_element_by_xpath("//*[local-name()='tspan'][text()=\"about the candidate\"]")
        bubblesix.click()
        time.sleep(4)
        goodinterviewsubmit = driver.find_element_by_xpath("(//a[text()=\"SUBMIT\"])[2]")
        goodinterviewsubmit.click()
        time.sleep(2)

        howhemispherecanhelp = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
        howhemispherecanhelp.click()
        time.sleep(1)
        howlongittakes = driver.find_element_by_xpath("//*[contains(text(), 'Start')]")
        howlongittakes.click()

        exampleexcercise = driver.find_element_by_xpath("//*[contains(text(), 'Go')]")
        exampleexcercise.click()
        time.sleep(5)
        activate_selector_audio = driver.find_element_by_xpath("//div[@class='interval-group audio']")
        activate_selector_audio.click()
        time.sleep(1)
        hover_over_audio = driver.find_element_by_xpath("//div[@class='selector']")
        hover_over_audio.click()
        time.sleep(1)
        finish_audio = driver.find_element_by_xpath("//*[contains(text(), 'Finish')]")
        finish_audio.click()
        time.sleep(1)

        activate_selector_video = driver.find_element_by_xpath("//div[@class='interval-group video']")
        activate_selector_video.click()
        time.sleep(5)
        hover_over_video = driver.find_element_by_xpath("//div[@class='selector']")
        hover_over_video.click()
        time.sleep(1)
        finish_video = driver.find_element_by_xpath("//*[contains(text(), 'Finish')]")
        finish_video.click()
        time.sleep(3)

        start_module_one = driver.find_element_by_xpath("//a[text()='START MODULE 1']")
        start_module_one.click()
        time.sleep(10)

        for i in range(11):
            activate_selector_audio = driver.find_element_by_xpath("//div[@class='interval-group audio']")
            activate_selector_audio.click()
            time.sleep(1)
            hover_over_audio = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_audio.click()
            time.sleep(1)
            next_audio = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_audio.click()
            time.sleep(10)

        start_distraction = driver.find_element_by_xpath("//a[text()='Start']")
        start_distraction.click()
        time.sleep(1)

        for i in range(6):
            distraction_question = driver.find_element_by_xpath("//a[@class='option-button correct ng-star-inserted']")
            distraction_question.click()
            next_distraction_question = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline "
                                                                     "hover active show']")
            next_distraction_question.click()
            time.sleep(1)

        start_video = driver.find_element_by_xpath("//a[text()='Start']")
        start_video.click()
        time.sleep(15)

        for i in range(11):
            activate_selector_video = driver.find_element_by_xpath("//div[@class='interval-group video']")
            activate_selector_video.click()
            time.sleep(5)
            hover_over_video = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_video.click()
            time.sleep(1)
            next_video = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_video.click()
            time.sleep(15)

        schoolvideowatch = driver.find_element_by_xpath("//span[text()='WATCH']")
        schoolvideowatch.click()
        time.sleep(70)
        finishschoolvideo = driver.find_element_by_xpath("//a[text()='COMPLETE MODULE']")
        finishschoolvideo.click()
        time.sleep(2)

        start_module_two = driver.find_element_by_xpath("//a[text()='Start']")
        start_module_two.click()
        time.sleep(10)

        for i in range(12):
            activate_selector_audio = driver.find_element_by_xpath("//div[@class='interval-group audio']")
            activate_selector_audio.click()
            time.sleep(1)
            hover_over_audio = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_audio.click()
            time.sleep(1)
            next_audio = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_audio.click()
            time.sleep(10)

        start_distraction_two = driver.find_element_by_xpath("//a[text()='Start']")
        start_distraction_two.click()
        time.sleep(1)

        for i in range(6):
            distraction_question = driver.find_element_by_xpath("//a[@class='option-button correct ng-star-inserted']")
            distraction_question.click()
            next_distraction_question = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline "
                                                                     "hover active show']")
            next_distraction_question.click()
            time.sleep(1)

        start_video_two = driver.find_element_by_xpath("//a[text()='Start']")
        start_video_two.click()
        time.sleep(15)

        for i in range(12):
            activate_selector_video = driver.find_element_by_xpath("//div[@class='interval-group video']")
            activate_selector_video.click()
            time.sleep(5)
            hover_over_video = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_video.click()
            time.sleep(1)
            next_video = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_video.click()
            time.sleep(15)

        results_next = driver.find_element_by_xpath("//a[text()='Next']")
        results_next.click()
        time.sleep(2)

        watch_econe = driver.find_element_by_xpath("//span[contains(text(),'WATCH')]")
        watch_econe.click()
        time.sleep(80)
        play_nextvideo = driver.find_element_by_xpath("//div[@class='play-next']")
        play_nextvideo.click()
        time.sleep(80)
        play_nextvideo.click()
        time.sleep(80)
        finish_ec = driver.find_element_by_xpath("//a[text()='COMPLETE MODULE']")
        finish_ec.click()
        time.sleep(2)

        start_module_three = driver.find_element_by_xpath("//a[text()='Start']")
        start_module_three.click()
        time.sleep(10)

        for i in range(11):
            activate_selector_audio = driver.find_element_by_xpath("//div[@class='interval-group audio']")
            activate_selector_audio.click()
            time.sleep(1)
            hover_over_audio = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_audio.click()
            time.sleep(1)
            next_audio = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_audio.click()
            time.sleep(10)

        start_distraction_three = driver.find_element_by_xpath("//a[text()='Start']")
        start_distraction_three.click()
        time.sleep(1)

        for i in range(6):
            distraction_question = driver.find_element_by_xpath("//a[@class='option-button correct ng-star-inserted']")
            distraction_question.click()
            next_distraction_question = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline "
                                                                     "hover active show']")
            next_distraction_question.click()
            time.sleep(1)

        start_video_three = driver.find_element_by_xpath("//a[text()='Start']")
        start_video_three.click()
        time.sleep(15)

        for i in range(11):
            activate_selector_video = driver.find_element_by_xpath("//div[@class='interval-group video']")
            activate_selector_video.click()
            time.sleep(5)
            hover_over_video = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_video.click()
            time.sleep(1)
            next_video = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_video.click()
            time.sleep(15)

        geographyvideowatch = driver.find_element_by_xpath("//span[text()='WATCH']")
        geographyvideowatch.click()
        time.sleep(70)
        finishgeographyvideo = driver.find_element_by_xpath("//a[text()='COMPLETE MODULE']")
        finishgeographyvideo.click()
        time.sleep(2)

        start_module_four = driver.find_element_by_xpath("//a[text()='Start']")
        start_module_four.click()
        time.sleep(10)

        for i in range(7):
            activate_selector_audio = driver.find_element_by_xpath("//div[@class='interval-group audio']")
            activate_selector_audio.click()
            time.sleep(1)
            hover_over_audio = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_audio.click()
            time.sleep(1)
            next_audio = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_audio.click()
            time.sleep(10)

        start_distraction_four = driver.find_element_by_xpath("//a[text()='Start']")
        start_distraction_four.click()
        time.sleep(1)

        for i in range(6):
            distraction_question = driver.find_element_by_xpath("//a[@class='option-button correct ng-star-inserted']")
            distraction_question.click()
            next_distraction_question = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline "
                                                                     "hover active show']")
            next_distraction_question.click()
            time.sleep(1)

        start_video_four = driver.find_element_by_xpath("//a[text()='Start']")
        start_video_four.click()
        time.sleep(15)

        for i in range(7):
            activate_selector_video = driver.find_element_by_xpath("//div[@class='interval-group video']")
            activate_selector_video.click()
            time.sleep(5)
            hover_over_video = driver.find_element_by_xpath("//div[@class='selector']")
            hover_over_video.click()
            time.sleep(1)
            next_video = driver.find_element_by_xpath("//a[@class='btn btn-outline-primary btn-outline hover']")
            next_video.click()
            time.sleep(15)

        results_next_two = driver.find_element_by_xpath("//a[text()='Next']")
        results_next_two.click()
        time.sleep(2)

        watch_ectwo = driver.find_element_by_xpath("//span[contains(text(),'WATCH')]")
        watch_ectwo.click()
        time.sleep(80)
        play_nextvideo = driver.find_element_by_xpath("//div[@class='play-next']")
        play_nextvideo.click()
        time.sleep(80)
        play_nextvideo.click()
        time.sleep(80)
        finish_ec = driver.find_element_by_xpath("//a[text()='COMPLETE MODULE']")
        finish_ec.click()
        time.sleep(2)

        log_out_dropdown = driver.find_element_by_id('dropdown02')
        log_out_dropdown.click()
        time.sleep(1)

        logout = driver.find_element_by_xpath("//a[text()='Logout']")
        logout.click()

        login_page = driver.find_element_by_xpath("//button[text()='Log in']").text
        assert 'LOG IN' in login_page


full_game = FullGame()
full_game.new_user_full_game()
