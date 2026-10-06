📄 Table: invoice_counters - InvoiceCounter - InvoiceCounters
Columns: year serial counter:integer

📄 Table: services - Service - Services
Columns: name

📄 Table: remittance_types - RemittanceType - RemittanceTypes
Columns: name

📄 Table: project_statuses - ProjectStatus - ProjectStatuses
Columns: name

📄 Table: customer_statuses - CustomerStatus - CustomerStatuses
Columns: name

📄 Table: product_types - ProductType - ProductTypes
Columns: name

📄 Table: systems - System - Systems
Columns: name status version

📄 Table: teams - Team - Teams
Columns: name description

📄 Table: quotes - Quote - Quotes
Columns: author feedback title

📄 Table: companies - Company - Companies
Columns: country_id:fk name tax address zip_code state municipality email phone website

📄 Table: own_companies - OwnCompany - OwnCompanies
Columns: country_id:fk name tax address zip_code state municipality email phone website

📄 Table: providers - Provider - Providers
Columns: service_id:fk code name

📄 Table: customers - Customer - Customers
Columns: company_id:fk customer_status_id:fk service_id:fk code

📄 Table: customer_invoices - CustomerInvoice - CustomerInvoices
Columns: customer_id:fk remittance_type_id:fk bank_name bank_account account_holder iban bic due_date:integer due_date_by_days:integer

📄 Table: projects - Project - Projects
Columns: customer_id:fk project_status_id:fk name total_hours:integer current_hours:integer started_at:timestamp finished_at:timestamp description

📄 Table: project_products - ProjectProduct - ProjectProducts
Columns: invoice_header_id:fk project_id:fk product_id:fk quantity:integer total_without_vat:decimal next_invoice_date:date

📄 Table: products - Product - Products
Columns: product_type_id:fk name unit_value:integer amount_without_vat:decimal description

📄 Table: invoice_headers - InvoiceHeader - InvoiceHeaders
Columns: invoice_counter_id:fk own_company_id:fk remittance_type_id:fk customer_id:fk invoice_string invoice_nb:integer invoice_date:date invoice_due_date:date year month amount_with_vat:decimal amount_without_vat:decimal vat_type:decimal vat_quote:decimal has_paid:boolean description

📄 Table: invoice_lines - InvoiceLine - InvoiceLines
Columns: invoice_header_id:fk vat_rated:decimal quantity:int unit_price:decimal amount_without_vat:decimal description
