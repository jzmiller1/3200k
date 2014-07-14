def print_lines(f):
    """ prints lines of text in give text file

    >>> print_lines('demotext.txt')
    Hello!
    Line 2
    This is line 3!

    """
    pass


def write_lines(f):
    """ writes user input to specified file

    # >>> write_lines('outputs.txt')
    # Enter some data: ABCD
    # Enter another line? [Y/n]y
    # Enter some data: abcd
    # Enter another line? [Y/n]n
    """
    pass


def show_tb_data():
    """ prints the lines of WHO TB data

    data from:
    http://www.who.int/tb/country/data/download/en/

    >>> show_tb_data() # doctest:+ELLIPSIS
    "country","iso2","iso3","iso_numeric","g_whoregion","year","e_pop_num","e_prev_100k","e_prev_100k_lo","e_prev_100k_hi","e_prev_num","e_prev_num_lo","e_prev_num_hi","e_mort_exc_tbhiv_100k","e_mort_exc_tbhiv_100k_lo","e_mort_exc_tbhiv_100k_hi","e_mort_exc_tbhiv_num","e_mort_exc_tbhiv_num_lo","e_mort_exc_tbhiv_num_hi","source_mort","e_inc_100k","e_inc_100k_lo","e_inc_100k_hi","e_inc_num","e_inc_num_lo","e_inc_num_hi","e_tbhiv_prct","e_tbhiv_prct_lo","e_tbhiv_prct_hi","e_inc_tbhiv_100k","e_inc_tbhiv_100k_lo","e_inc_tbhiv_100k_hi","e_inc_tbhiv_num","e_inc_tbhiv_num_lo","e_inc_tbhiv_num_hi","source_tbhiv","c_cdr","c_cdr_lo","c_cdr_hi"
    "Afghanistan","AF","AFG","004","EMR",1990,11731193,327,112,655,38000,13000,77000,31,7.3,72,3700,860,8500,"Indirect",189,117,279,22000,14000,33000,0.18,,,0.35,0.22,0.52,41,25,60,"Model",20,13,32
    ...
    "Zimbabwe","ZW","ZWE","716","AFR",2012,13724317,433,92,1034,59000,13000,140000,33,1.2,117,4600,160,16000,"Indirect",562,434,706,77000,60000,97000,71,71,71,399,308,501,55000,42000,69000,"Surveillance",46,37,60
    """
    pass


def tb_per_100k(country):
    """
    show "e_inc_100k" by year for a given country

    >>> tb_per_100k("Afghanistan") # doctest:+ELLIPSIS
    ('1990', '189')
    ...
    ('2012', '189')
    """
    pass


