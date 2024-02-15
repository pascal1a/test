from dash import Dash, dcc, html, Input, Output, callback
import os
import datetime


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    #body
    html.Div([
        #main
        html.Main([
            #html.Div(style = {  'height': '500px',
            #                    'display': 'hidden'}
                
                #html.Div([
                    #dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    #    <svg viewBox="25 25 50 50">
                    #        <circle cx="50" cy="50" r="20" fill="none" stroke-width="2" stroke-miterlimit="10" />    
                    #    </svg>
                    #    ''')
            
                    #], className='page-loader__spinner'),
            #    , className='page-loader'),     
            
            #header
            html.Header([
                html.Div([
                    html.I([
                        ], className='zwicon-hamburger-menu'),
                    ], className='avigation-trigger d-xl-none'),
                html.Div([
                    html.A('Crypto Data', href='/apps/home'),
                    ], className='logo d-none d-sm-inline-flex'),

                html.Ul([

                    html.Li([
                        html.A(html.I([
                            ], className='zwicon-refresh-double'), href='',
                            className='top-nav__notify'),   
                        ], className='dropdown top-nav__notifications'),
                ], className='top-nav'),

                ], className='header'),
            #Nav Bar
            html.Aside([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Img(
                                    className='user__img',
                                    src=app.get_asset_url('8.jpg'),
                                    ),
                                html.Div(["test user"
                                    ], className='user__name'),
                                html.Div(["test_user@gmail.com"
                                    ], className='user__email'),    
                                ]),
                            ], className='user__info'),
                       ], className='user'), 
                
                    html.Ul([
                        html.Li([
                            html.A([
                                html.I(
                                    className='zwicon-home'),
                                "Home"], 
                                href='/apps/home'),
                            ],
                            className='navigation__active'
                            ),
                        
                        html.Li([
                                html.A([
                                    html.I(
                                        className='zwicon-three-h'),
                                    "Derivatives"], 
                                    href='/apps/derivatives',
                                    id = "nav_bar_2"),

                                html.Ul([
                                    html.Li([
                                        html.A(
                                            "Exchanges Overview",
                                            href="/apps/derivatives"
                                            )
                                        ]),

                                    html.Li([
                                        html.A(
                                            "Derivatives Insights",
                                            href='/apps/derivatives_insights'
                                            )
                                        ]),

                                ],
                                id = 'nav_bar_2_drop2',
                                style = {'display':'inline'}
                                ),

                            ], className='navigation__sub'),
                        
                        html.Li([
                                html.A([
                                    html.I(
                                        className='zwicon-repository'),
                                    "Blockchain"], 
                                    href='/apps/addresses',
                                    id = "nav_bar_3"),

                                html.Ul([
                                    html.Li([
                                        html.A(
                                            "Addresses",
                                            href="/apps/addresses"
                                            )
                                        ]),

                                    html.Li([
                                        html.A(
                                            "Transactions",
                                            href='/apps/transactions'
                                            )
                                        ]),

                                    html.Li([
                                        html.A(
                                            "Difficulty, Hashrate, Blocks & Supply",
                                            href="/apps/difficulty"
                                            )
                                        ])


                                ],
                                id = 'nav_bar_2_drop',
                                style = {'display':'inline'}
                                ),

                            ], className='navigation__sub'),


                 


                        ], className='navigation'),



                    ], className='scrollbar'), 
                ], className='sidebar'),

            html.Div([
                html.Div([
                    ], className='scrollbar'),
                ], className='themes'),



            html.Section([
                html.Header([ 
                    html.H1(["Overview TOP Cryptocurrencies 30 DAYS",
                    #html.Small("Test")
                        ]), 
                    html.Div([
                        

                        html.A(
                            href="",
                            className = 'actions__item zwicon-refresh-double'),    
                        


                        ], className='actions'),
                    ], className='content__title'),

                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Bitcoin"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ]
                                ,className='quick-stats__info'
                                ),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    #'display': 'flex',
                                    #'autosize': True,
                                    #'use_container_width': True,
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                #,className='quick-stats__info'
                                ),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),
                    
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Ethereum"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                #,className='quick-stats__info'
                                ),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),

                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("BNB"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                ,className='quick-stats__info'),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'), 

                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Cardano"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                ,className='quick-stats__info'),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),  
                    
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Tether"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                ,className='quick-stats__info'),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),
                    
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Solano"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                ,className='quick-stats__info'),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),

                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Ripple"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                ,className='quick-stats__info'),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),

                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Polkadot"),
                                html.P(),
                                html.H2(),
                                html.Small(),
                                ], className='quick-stats__info'),  
                            html.Div([
                                ]
                                ,style = {
                                    'padding-left': '1rem',
                                    'padding-right': '1rem',
                                    'width':'80%',
                                }
                                ,className='quick-stats__info'),
                            ], className='quick-stats__item'),
                        ], className='col-sm-6 col-md-3'),

                    ], className='row quick-stats'),
                
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.H4("Top 10 Market capitalization: Relative Comparison (in %)"),
                                    ], className='card-title'),
                                html.Div([
                                    html.H6('Click on the legend to remove or add a currency for comparison'),
                                    ], className='card-subtitle'),
                                html.Div([
                                    ]   
                                    ),
                                html.Div([
                                    ], className='flot-chart-legends flot-chart-legends--curved'),    

                                ], className='card-body'),
                            ], className='card'),
                        ], className='col-lg-6'),


                            html.Div([

                                html.Div([
                                    
                                    html.Div([
                                            html.Div([
                                                html.H4("Price Forecasts: Bitcoin"),
                                                ], className='card-title'),
                                            html.Div([
                                                html.A("By Digitalcoin", href='https://digitalcoinprice.com/forecast/bitcoin'),
                                                ], className='card-subtitle'),
                                            
                                            html.Table([
                                                html.Thead(
                                                    html.Tr([
                                                        html.Th('Year'),
                                                        html.Th('Target'),
                                                        html.Th('Source'),
                                                    ])
                                                ),
                                            html.Tbody(
                                                    html.Tr([
                                                        html.Th("2022"),
                                                        html.Th("57'750$"),
                                                        html.Th('Digitalcoin'),
                                                    ])
                                                ),
                                            html.Tbody(
                                                    html.Tr([
                                                        html.Th("2023"),
                                                        html.Th("65'793$"),
                                                        html.Th('Digitalcoin'),
                                                    ])
                                                ), 
                                            html.Tbody(
                                                    html.Tr([
                                                        html.Th("2024"),
                                                        html.Th("73'923$"),
                                                        html.Th('Digitalcoin'),
                                                    ])
                                                ),
                                            html.Tbody(
                                                    html.Tr([
                                                        html.Th("2025"),
                                                        html.Th("90'605$"),
                                                        html.Th('Digitalcoin'),
                                                    ])
                                                ),

                                            html.Tbody(
                                                    html.Tr([
                                                        html.Th("2026"),
                                                        html.Th("$84'696$"),
                                                        html.Th('Digitalcoin'),
                                                    ])
                                                ),               
                                            

                                                ], className='table mb-0'),
                                            
                                            html.Div([
                                                html.H4("", style = {'display':'block', 'height':'300'}),
                                                
                                            ], style = {'display':'block', 'height':'69.9px'}       
                                            )

                                        ], className='card-body'),
                                        
                                    ], className='card'),
                        ], className='col-lg-6'),    
                    ], className='row'),    
    
                

            html.Div([
                html.Div([
                    html.Div([
                            html.Div([
                                html.H4("Recent Stats: Bitcoin"),
                                ], className='card-title'),
                            html.Div([
                                html.A("By Coingecko", href='https://www.coingecko.com/en/coins/bitcoin'),
                                ], className='card-subtitle'),
                        ], className='card-body'),

                    #html.Div([
                    #    html.Div([
                    #    
                    #        ], 
                    #        style = {
                    #                'position': 'relative',
                    #            },
                    #        className='flot-chart flot-chart--sm flot-past-days'),
                    #    ], className='widget-past-days__main'),

                    html.Div([

                        html.Div([
                            html.Div([
                                html.Small("Market Cap"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Market Cap Rank"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Market Cap Change 24h"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Market Cap Change 24h in %"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Price Change 24h"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Price Change 24h in %"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Circulating Supply"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Max. Supply"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),


                        ], className='listview listview--striped'),
                    ], className='card widget-past-days'),    
                html.Div([
                    html.Div([
                            html.Div([
                                html.H4("Recent Stats: Ethereum"),
                                ], className='card-title'),
                            html.Div([
                                html.A("By Coingecko", href='https://www.coingecko.com/en/coins/bitcoin'),
                                ], className='card-subtitle'),
                        ], className='card-body'),

                    html.Div([

                        html.Div([
                            html.Div([
                                html.Small("Market Cap"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Market Cap Rank"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Market Cap Change 24h"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Market Cap Change 24h in %"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Price Change 24h"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Price Change 24h in %"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Circulating Supply"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Max. Supply"),
                                html.H3("-"),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),


                        ], className='listview listview--striped'),        

                    ], className='card widget-past-days'),

                html.Div([
                    html.Div([
                            html.Div([
                                html.H4("Recent Stats: Binance Coin"),
                                ], className='card-title'),
                            html.Div([
                                html.A("By Coingecko", href='https://www.coingecko.com/en/coins/bitcoin'),
                                ], className='card-subtitle'),
                        ], className='card-body'),

                    html.Div([

                        html.Div([
                            html.Div([
                                html.Small("Market Cap"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Market Cap Rank"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Market Cap Change 24h"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Market Cap Change 24h in %"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Price Change 24h"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Price Change 24h in %"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),

                        html.Div([
                            html.Div([
                                html.Small("Circulating Supply"),
                                html.H3(),
                                ], className='widget-past-days__info'),
                            html.Div([
                                html.Small("Max. Supply"),
                                html.H3(),
                                ], className='widget-past-days__chart hidden-sm'),

                            ], className='listview__item'),


                        ], className='listview listview--striped'),        

                    ], className='card widget-past-days'),

                ], className='widget-lists card-columns'),
            
            html.Div([
                html.Div([
                    html.Div([
                        html.H4("Correlation Matrix past 3Y"),
                        ], className='card-title'),
                    dcc.Checklist(
                        id='medals12',
                        options=[],
                        value=0,
                        style={"display": "grid", "grid-template-columns": "repeat(auto-fill, minmax(100px, 120px))"},
                        inputStyle={"margin-right": "5px"},
                    ),
                    html.Div(id = "correlation_id"),    
                    ], className='card-body'),
                ], className='card'),

            html.Div([
                    html.Div([
                            html.Div([
                                html.H4("Select Currency"),
                                ], style={'text-align': 'center'}, className='card-title'),
                            html.Div([
                                html.H6(""),
                                ], className='card-subtitle'),
                            html.Div([
                                dcc.Dropdown(
                                    id='demo-dropdown',
                                    options=[
                                        {'label': 'Bitcoin', 'value': 'bitcoin'},
                                        {'label': 'Ethereum', 'value': 'ethereum'},
                                        {'label': 'BNB', 'value': 'binancecoin'},
                                        {'label': 'Cardano', 'value': 'cardano'},
                                        {'label': 'Solana', 'value': 'solana'},
                                        {'label': 'Ripple', 'value': 'ripple'}
                                    ],
                                    value='bitcoin'
                                )
                                 
                                
                            ], style={'text-align': 'center'}),


                            html.Div([
                                html.H4("Select Benchmark"),
                                ], style={'text-align': 'center', 'margin-top': '5px'}, className='card-title'),
                            html.Div([
                                html.H6(""),
                                ], className='card-subtitle'),
                            html.Div([
                                dcc.Dropdown(
                                    id='demo-dropdown-2',
                                    options=[
                                        {'label': 'Bitcoin', 'value': 'bitcoin'},
                                        {'label': 'Ethereum', 'value': 'ethereum'},
                                        {'label': 'BNB', 'value': 'binancecoin'},
                                        {'label': 'Cardano', 'value': 'cardano'},
                                        {'label': 'Solana', 'value': 'solana'},
                                        {'label': 'Ripple', 'value': 'ripple'}
                                    ],
                                    value='ethereum'
                                ),
                                html.Div(id='dd-output-container-2', 
                                style={'height': 30,'text-align': 'center'})
                            ], style={'text-align': 'center'}),


                        ], className='card-body'),
                    ], className='card'), 
                
                html.Div([
                    html.Div([
                            html.Div([
                                html.H4("Select Date Range"),
                                ], style={'text-align': 'center'}, className='card-title'),
                            html.Div([
                                html.H6(""),
                                ], className='card-subtitle'),
                            html.Div([
                                dcc.DatePickerRange(
                                    id='my-date-picker-range',
                                    min_date_allowed=datetime.date(2015, 8, 5),
                                    max_date_allowed=datetime.date(2020, 9, 19),
                                    #initial_visible_month=datetime.date(2017, 8, 5),
                                    end_date=datetime.date(2019, 8, 25),
                                    start_date=datetime.date(2017, 8, 5),
                                    number_of_months_shown = 4
                                ),
                                html.Div(id='output-container-date-picker-range', 
                                style={'height': 30,'text-align': 'center'})
                            ], style={'text-align': 'center'}),    
                            
                        ], className='card-body'),
                    ], className='card'), 
                html.Div([
                    html.Div([
                            html.Div([
                                html.H4("Historical Price"),
                                ], style={'text-align': 'center'}, className='card-title'),
                            html.Div([
                                html.H6(""),
                                ], className='card-subtitle'),
                            html.Div([

                                dcc.Graph(id="graph_2"),
                                #dbc.Button(
                                #    id="submit_button",
                                #    n_clicks=0,
                                #    children="Submit",
                                #    color="primary",
                                #    
                                #)
                            ]),
                        ], className='card-body'),
                    ], className='card'),       

                html.Div([
                    html.Div([
                        html.Div([
                                html.H4("Risk and Performance Measures"),
                                ], style={'text-align': 'center'}, className='card-title'),

                        # Row 1
                        html.Div([
                            
                            html.Div([
                                html.Div([
                                    html.Small("Annualized Return"),
                                    html.H3(id='annual_return_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Cumulative Return"),
                                    html.H3(id='cummulative_return_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Annualized Volatility"),
                                    html.H3(id = "volatility_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Maximum Drawdown"),
                                    html.H3(id = "drawdown_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            ], className='row invoice__attrs'),
                        # Row 2
                        html.Div([
                            
                            html.Div([
                                html.Div([
                                    html.Small("Alpha (Benchmark Outperformance)"),
                                    html.H3(id = "alpha_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Beta (Compared to Benchmark)"),
                                    html.H3(id='beta_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Skew"),
                                    html.H3(id = "skew_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Kurtosis"),
                                    html.H3(id = "kurtosis_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            ], className='row invoice__attrs'),

                        # Row 3
                        html.Div([
                            
                            html.Div([
                                html.Div([
                                    html.Small("Sharpe Ratio"),
                                    html.H3(id ="sharpe_ratio_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Treynor Ratio"),
                                    html.H3(id ="treynor_ratio_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Information Ratio"),
                                    html.H3(id ="information_ratio_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Modigliani-Miller Ratio"),
                                    html.H3(id ="modigliani_miller_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            ], className='row invoice__attrs'),
                        
                        # Row 4
                        html.Div([
                            
                            html.Div([
                                html.Div([
                                    html.Small("Value at Risk (1 Day, 99%, historical)"),
                                    html.H3(id='VaR_1d_hist_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Value at Risk (10 Days, 99%, historical)"),
                                    html.H3(id='VaR_10d_hist_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Value at Risk (1 Day, 99%, gaussian distribution)"),
                                    html.H3(id ="VaR_1d_gauss_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Value at Risk (10 Day, 99%, gaussian distribution)"),
                                    html.H3(id = "VaR_10d_gauss_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            ], className='row invoice__attrs'),

                        # Row 5
                        html.Div([
                            
                            html.Div([
                                html.Div([
                                    html.Small("Value at Risk (1 Day, 99%, Cornish Fisher )"),
                                    html.H3(id='var_1d_fisher_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Value at Risk (10 Day, 99%, Cornish Fisher )"),
                                    html.H3(id='var_10d_fisher_id'),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Conditional Value at Risk (1 Day, 99%, historical)"),
                                    html.H3(id = "cvar_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            html.Div([
                                html.Div([
                                    html.Small("Lower Partial Moment"),
                                    html.H3(id = "lower_partial_moment_id"),
                                    ], className='invoice__attrs__item'),
                                ], className='col-3'),

                            ], className='row invoice__attrs'),

                               
        

                        ], className='card-body'),

                    ], className='card'),






            ], className='content'),
            
            html.Div([
                
                html.Div([           
                    ], className='page-loader__spinner'),
            ], className='page-loader'),  

            ], className='main'),

          
        ], className='data-sa-theme-new'),
    ])

@callback(Output('display-value', 'children'), Input('dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run(debug=True)