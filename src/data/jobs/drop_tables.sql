
/**
Drop all views and tables
**/

drop view if exists public.top_senator_gains_from_purchases;
drop view if exists public.top_senator_gains_from_sales;
drop view if exists top_senator_losses_from_purchases;
drop view if exists top_senator_losses_from_sales;

drop view if exists company_metrics_view;
drop view if exists senator_trades_view;
drop view if exists top_industries_view;

drop table if exists senator_trades cascade;
drop table if exists senators cascade;
drop table if exists company_annual_financial_data cascade;
drop table if exists company_historical_data cascade;
drop table if exists company_profiles cascade;
