import datetime


def which_date(start_date, time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """

    ori_date = start_date.split("/")
    ori_date = list(map(int, ori_date))
    ori_date = datetime.date(ori_date[0], ori_date[1], ori_date[2])
    delay_date = time.split(" ")
    delay_date[0] = int(delay_date[0])
    if "days" in delay_date:
        end_date = ori_date + datetime.timedelta(days=delay_date[0])
    else:
        end_date = ori_date + datetime.timedelta(weeks=delay_date[0])

    year = str(end_date.year)
    month = str(end_date.month)
    day = str(end_date.day)
    if end_date.month < 10:
        month = "0" + month
    if end_date.day < 10:
        day = "0" + day
    end_date = year + "/" + month + "/" + day

    return end_date


def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10', '35 days') == '2016/03/16'
    assert which_date('2016/12/21', '3 weeks') == '2017/01/11'
    assert which_date('2015/01/17', '1 week') == '2015/01/24'
    print("All tests completed.")


if __name__ == "__main__":
    test()