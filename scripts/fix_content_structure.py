from __future__ import annotations

import json
import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
CONTENT_DIR = BASE_DIR / "content"

TABS = [
    {"code": "theory", "title": "الشرح النظري", "type": "markdown", "file": "theory.md"},
    {"code": "examples", "title": "الأمثلة", "type": "markdown", "file": "examples.md"},
    {"code": "essay", "title": "أسئلة مقالية", "type": "markdown", "file": "essay.md"},
    {"code": "mistakes", "title": "أخطاء شائعة", "type": "markdown", "file": "mistakes.md"},
    {"code": "mcq", "title": "اختيار من متعدد", "type": "quiz", "file": "mcq.json"},
]


def leaf(folder: str, code: str, slug: str, title: str) -> dict:
    return {"folder": folder, "code": code, "slug": slug, "title": title, "leaf": True}


def node(folder: str, code: str, slug: str, title: str, children: list[dict]) -> dict:
    return {"folder": folder, "code": code, "slug": slug, "title": title, "children": children}


TREE = [
    node("01-accounting-framework", "1", "accounting-framework", "الإطار العام للمحاسبة المالية", [
        node("01-nature-of-accounting-and-reporting", "1.1", "nature-of-accounting-and-reporting", "طبيعة المحاسبة والتقارير المالية", [
            leaf("01-nature-and-objectives", "1.1.1", "nature-and-objectives", "طبيعة المحاسبة المالية وأهدافها"),
            leaf("02-users-and-needs", "1.1.2", "users-and-needs", "مستخدمو القوائم المالية واحتياجاتهم"),
            leaf("03-reporting-objectives", "1.1.3", "reporting-objectives", "أهداف التقارير المالية"),
            leaf("04-role-in-decision-making", "1.1.4", "role-in-decision-making", "دور المعلومات المحاسبية في اتخاذ القرار"),
            leaf("05-recordkeeping-and-system", "1.1.5", "recordkeeping-and-system", "مسك السجلات والنظام المحاسبي"),
        ]),
        node("02-accounting-principles-and-standards", "1.2", "accounting-principles-and-standards", "المبادئ والمعايير المحاسبية", [
            leaf("01-basic-principles-and-assumptions", "1.2.1", "basic-principles-and-assumptions", "المبادئ والفروض المحاسبية الأساسية"),
            leaf("02-ias", "1.2.2", "ias", "معايير المحاسبة الدولية IAS"),
            leaf("03-ifrs", "1.2.3", "ifrs", "معايير التقارير المالية الدولية IFRS"),
            leaf("04-iasb-role", "1.2.4", "iasb-role", "دور IASB في إصدار المعايير"),
            leaf("05-global-harmonization", "1.2.5", "global-harmonization", "تجانس المعايير المحاسبية دولياً"),
            leaf("06-sme-standards", "1.2.6", "sme-standards", "المعايير الخاصة بالمنشآت الصغيرة والمتوسطة"),
        ]),
        node("03-conceptual-framework", "1.3", "conceptual-framework", "الإطار النظري للمحاسبة المالية", [
            leaf("01-framework-concept-and-importance", "1.3.1", "framework-concept-and-importance", "مفهوم وأهمية الإطار النظري"),
            leaf("02-accounting-information-characteristics", "1.3.2", "accounting-information-characteristics", "خصائص المعلومات المحاسبية"),
            leaf("03-substance-over-form", "1.3.3", "substance-over-form", "الجوهر الاقتصادي مقابل الشكل القانوني"),
            leaf("04-policies-estimates-errors", "1.3.4", "policies-estimates-errors", "السياسات المحاسبية والتقديرات والأخطاء"),
            leaf("05-treatment-without-direct-standard", "1.3.5", "treatment-without-direct-standard", "المعالجة المحاسبية عند عدم وجود معيار مباشر"),
        ]),
    ]),
    node("02-basic-accounting-concepts", "2", "basic-accounting-concepts", "المفاهيم المحاسبية الأساسية", [
        leaf("01-accounting-entity", "2.1", "accounting-entity", "الوحدة المحاسبية"),
        leaf("02-monetary-unit", "2.2", "monetary-unit", "وحدة القياس النقدي"),
        leaf("03-going-concern", "2.3", "going-concern", "الاستمرارية"),
        leaf("04-accounting-period", "2.4", "accounting-period", "الفترة المحاسبية"),
        leaf("05-historical-cost", "2.5", "historical-cost", "التكلفة التاريخية"),
        leaf("06-verifiability", "2.6", "verifiability", "التحقق"),
        leaf("07-matching", "2.7", "matching", "المقابلة"),
        leaf("08-conservatism", "2.8", "conservatism", "التحفظ"),
        leaf("09-consistency", "2.9", "consistency", "الاتساق"),
        leaf("10-materiality", "2.10", "materiality", "الأهمية النسبية"),
    ]),
    node("03-financial-statements", "3", "financial-statements", "القوائم المالية الأساسية", [
        node("01-statement-of-financial-position", "3.1", "statement-of-financial-position", "قائمة المركز المالي", [
            leaf("01-current-assets-cash", "3.1.1", "current-assets-cash", "الأصول المتداولة - النقدية وما في حكمها"),
            leaf("02-current-assets-receivables", "3.1.2", "current-assets-receivables", "الأصول المتداولة - الذمم المدينة"),
            leaf("03-current-assets-inventory", "3.1.3", "current-assets-inventory", "الأصول المتداولة - المخزون"),
            leaf("04-current-assets-prepaid-expenses", "3.1.4", "current-assets-prepaid-expenses", "الأصول المتداولة - المصروفات المقدمة"),
            leaf("05-current-assets-short-term-investments", "3.1.5", "current-assets-short-term-investments", "الأصول المتداولة - الاستثمارات قصيرة الأجل"),
            leaf("06-non-current-assets-ppe", "3.1.6", "non-current-assets-ppe", "الأصول غير المتداولة - الممتلكات والآلات والمعدات"),
            leaf("07-non-current-assets-fixed-assets", "3.1.7", "non-current-assets-fixed-assets", "الأصول غير المتداولة - الأصول الثابتة وإهلاكها"),
            leaf("08-non-current-assets-natural-resources", "3.1.8", "non-current-assets-natural-resources", "الأصول غير المتداولة - الموارد الطبيعية واستنفادها"),
            leaf("09-non-current-assets-intangibles", "3.1.9", "non-current-assets-intangibles", "الأصول غير المتداولة - الأصول غير الملموسة"),
            leaf("10-non-current-assets-rd", "3.1.10", "non-current-assets-rd", "الأصول غير المتداولة - البحث والتطوير"),
            leaf("11-non-current-assets-long-term-investments", "3.1.11", "non-current-assets-long-term-investments", "الأصول غير المتداولة - الاستثمارات طويلة الأجل"),
            leaf("12-current-liabilities-suppliers", "3.1.12", "current-liabilities-suppliers", "الالتزامات المتداولة - الموردون"),
            leaf("13-current-liabilities-accrued-expenses", "3.1.13", "current-liabilities-accrued-expenses", "الالتزامات المتداولة - المصروفات المستحقة"),
            leaf("14-current-liabilities-short-term-loans", "3.1.14", "current-liabilities-short-term-loans", "الالتزامات المتداولة - القروض قصيرة الأجل"),
            leaf("15-current-liabilities-taxes", "3.1.15", "current-liabilities-taxes", "الالتزامات المتداولة - الضرائب المستحقة"),
            leaf("16-long-term-liabilities-loans", "3.1.16", "long-term-liabilities-loans", "الالتزامات طويلة الأجل - القروض طويلة الأجل"),
            leaf("17-long-term-liabilities-bonds", "3.1.17", "long-term-liabilities-bonds", "الالتزامات طويلة الأجل - السندات"),
            leaf("18-long-term-liabilities-finance-lease", "3.1.18", "long-term-liabilities-finance-lease", "الالتزامات طويلة الأجل - التأجير التمويلي"),
            leaf("19-long-term-liabilities-deferred-taxes", "3.1.19", "long-term-liabilities-deferred-taxes", "الالتزامات طويلة الأجل - الضرائب المؤجلة"),
            leaf("20-long-term-liabilities-contingencies", "3.1.20", "long-term-liabilities-contingencies", "الالتزامات طويلة الأجل - الالتزامات الطارئة"),
            leaf("21-equity-capital", "3.1.21", "equity-capital", "حقوق الملكية - رأس المال"),
            leaf("22-equity-common-and-preferred-shares", "3.1.22", "equity-common-and-preferred-shares", "حقوق الملكية - الأسهم العادية والممتازة"),
            leaf("23-equity-treasury-shares", "3.1.23", "equity-treasury-shares", "حقوق الملكية - أسهم الخزينة"),
            leaf("24-equity-reserves", "3.1.24", "equity-reserves", "حقوق الملكية - الاحتياطيات"),
            leaf("25-equity-retained-earnings", "3.1.25", "equity-retained-earnings", "حقوق الملكية - الأرباح المحتجزة"),
            leaf("26-equity-dividends", "3.1.26", "equity-dividends", "حقوق الملكية - توزيعات الأرباح"),
            leaf("27-equity-eps", "3.1.27", "equity-eps", "حقوق الملكية - نصيب السهم من الأرباح"),
            leaf("28-related-financial-position-changes", "3.1.28", "related-financial-position-changes", "موضوعات مرتبطة بقائمة المركز المالي - التغيرات المؤثرة على المركز المالي"),
            leaf("29-related-disclosure-ias1", "3.1.29", "related-disclosure-ias1", "موضوعات مرتبطة بقائمة المركز المالي - الإفصاح والعرض وفق IAS 1"),
            leaf("30-related-english-terms", "3.1.30", "related-english-terms", "موضوعات مرتبطة بقائمة المركز المالي - مصطلحات قائمة المركز المالي باللغة الإنجليزية"),
        ]),
        node("02-income-statement", "3.2", "income-statement", "قائمة الدخل", [
            leaf("01-elements-revenue", "3.2.1", "elements-revenue", "عناصر قائمة الدخل - الإيرادات"),
            leaf("02-elements-cost-of-sales", "3.2.2", "elements-cost-of-sales", "عناصر قائمة الدخل - تكلفة المبيعات"),
            leaf("03-elements-gross-profit", "3.2.3", "elements-gross-profit", "عناصر قائمة الدخل - مجمل الربح"),
            leaf("04-elements-operating-expenses", "3.2.4", "elements-operating-expenses", "عناصر قائمة الدخل - المصاريف التشغيلية"),
            leaf("05-elements-gains-and-losses", "3.2.5", "elements-gains-and-losses", "عناصر قائمة الدخل - الأرباح والخسائر"),
            leaf("06-elements-net-income", "3.2.6", "elements-net-income", "عناصر قائمة الدخل - صافي الربح"),
            leaf("07-related-nature-of-income", "3.2.7", "related-nature-of-income", "موضوعات مرتبطة بقائمة الدخل - طبيعة الدخل"),
            leaf("08-related-expense-recognition", "3.2.8", "related-expense-recognition", "موضوعات مرتبطة بقائمة الدخل - الاعتراف بالمصروفات"),
            leaf("09-related-economic-income", "3.2.9", "related-economic-income", "موضوعات مرتبطة بقائمة الدخل - الدخل الاقتصادي"),
            leaf("10-related-accrual-vs-cash", "3.2.10", "related-accrual-vs-cash", "موضوعات مرتبطة بقائمة الدخل - أساس الاستحقاق مقابل الأساس النقدي"),
            leaf("11-related-retained-earnings", "3.2.11", "related-retained-earnings", "موضوعات مرتبطة بقائمة الدخل - الأرباح المحتجزة"),
            leaf("12-related-link-to-financial-position", "3.2.12", "related-link-to-financial-position", "موضوعات مرتبطة بقائمة الدخل - العلاقة بين قائمة الدخل وقائمة المركز المالي"),
            leaf("13-related-disclosure-ias1", "3.2.13", "related-disclosure-ias1", "موضوعات مرتبطة بقائمة الدخل - الإفصاح والعرض وفق IAS 1"),
            leaf("14-related-english-terms", "3.2.14", "related-english-terms", "موضوعات مرتبطة بقائمة الدخل - مصطلحات قائمة الدخل باللغة الإنجليزية"),
        ]),
        node("03-cash-flow-statement", "3.3", "cash-flow-statement", "قائمة التدفقات النقدية", [
            leaf("01-cash-and-equivalents", "3.3.1", "cash-and-equivalents", "مفهوم النقد والنقد المعادل"),
            leaf("02-operating-cash-flows", "3.3.2", "operating-cash-flows", "التدفقات التشغيلية"),
            leaf("03-investing-cash-flows", "3.3.3", "investing-cash-flows", "التدفقات الاستثمارية"),
            leaf("04-financing-cash-flows", "3.3.4", "financing-cash-flows", "التدفقات التمويلية"),
            leaf("05-direct-method", "3.3.5", "direct-method", "إعداد القائمة بالطريقة المباشرة"),
            leaf("06-indirect-method", "3.3.6", "indirect-method", "إعداد القائمة بالطريقة غير المباشرة"),
            leaf("07-analysis", "3.3.7", "analysis", "تحليل قائمة التدفقات النقدية"),
            leaf("08-disclosure-ias7", "3.3.8", "disclosure-ias7", "الإفصاح وفق IAS 7"),
        ]),
        node("04-statement-of-changes-in-equity", "3.4", "statement-of-changes-in-equity", "قائمة التغيرات في حقوق الملكية", [
            leaf("01-capital-changes", "3.4.1", "capital-changes", "التغيرات في رأس المال"),
            leaf("02-reserve-changes", "3.4.2", "reserve-changes", "التغيرات في الاحتياطيات"),
            leaf("03-retained-earnings", "3.4.3", "retained-earnings", "الأرباح المحتجزة"),
            leaf("04-effect-of-policies-and-errors", "3.4.4", "effect-of-policies-and-errors", "أثر السياسات المحاسبية والأخطاء"),
        ]),
    ]),
    node("04-revenue-and-cash", "4", "revenue-and-cash", "الإيرادات والنقدية", [
        node("01-revenue-recognition", "4.1", "revenue-recognition", "الاعتراف بالإيراد", [
            leaf("01-timing", "4.1.1", "timing", "توقيت الاعتراف بالإيراد"),
            leaf("02-conditions", "4.1.2", "conditions", "شروط الاعتراف بالإيراد"),
            leaf("03-sale-of-goods", "4.1.3", "sale-of-goods", "الإيراد من بيع السلع"),
            leaf("04-long-term-contracts", "4.1.4", "long-term-contracts", "الإيراد من العقود طويلة الأجل"),
            leaf("05-percentage-of-completion", "4.1.5", "percentage-of-completion", "نسبة الإنجاز"),
            leaf("06-production-method", "4.1.6", "production-method", "طريقة الإنتاج"),
            leaf("07-installment-method", "4.1.7", "installment-method", "طريقة التقسيط"),
        ]),
        node("02-cash-and-cash-assets", "4.2", "cash-and-cash-assets", "النقدية والأصول النقدية", [
            leaf("01-cash-and-equivalents", "4.2.1", "cash-and-equivalents", "النقدية وما في حكمها"),
            leaf("02-cash-control", "4.2.2", "cash-control", "الرقابة على النقدية"),
            leaf("03-liquidity-analysis", "4.2.3", "liquidity-analysis", "تحليل السيولة"),
            leaf("04-current-ratio", "4.2.4", "current-ratio", "نسبة التداول"),
        ]),
    ]),
    node("05-inventory-and-cost-of-sales", "5", "inventory-and-cost-of-sales", "المخزون وتكلفة المبيعات", [
        node("01-inventory-in-trading-companies", "5.1", "inventory-in-trading-companies", "المخزون في المنشآت التجارية", [
            leaf("01-acquisition-cost", "5.1.1", "acquisition-cost", "تكلفة الاقتناء"),
            leaf("02-periodic-inventory", "5.1.2", "periodic-inventory", "الجرد الدوري"),
            leaf("03-perpetual-inventory", "5.1.3", "perpetual-inventory", "الجرد المستمر"),
            leaf("04-retail-inventory", "5.1.4", "retail-inventory", "مخزون التجزئة"),
        ]),
        node("02-inventory-in-manufacturing-companies", "5.2", "inventory-in-manufacturing-companies", "المخزون في المنشآت الصناعية", [
            leaf("01-raw-materials", "5.2.1", "raw-materials", "المواد الخام"),
            leaf("02-work-in-process", "5.2.2", "work-in-process", "الإنتاج تحت التشغيل"),
            leaf("03-finished-goods", "5.2.3", "finished-goods", "الإنتاج التام"),
            leaf("04-cost-of-goods-manufactured", "5.2.4", "cost-of-goods-manufactured", "تكلفة السلع المصنعة"),
            leaf("05-cost-of-goods-sold", "5.2.5", "cost-of-goods-sold", "تكلفة السلع المباعة"),
        ]),
        node("03-inventory-pricing-methods", "5.3", "inventory-pricing-methods", "طرق تسعير المخزون", [
            leaf("01-specific-identification", "5.3.1", "specific-identification", "التعيين المحدد"),
            leaf("02-weighted-average", "5.3.2", "weighted-average", "المتوسط المرجح"),
            leaf("03-fifo", "5.3.3", "fifo", "الوارد أولاً صادر أولاً FIFO"),
            leaf("04-lifo", "5.3.4", "lifo", "الوارد أخيراً صادر أولاً LIFO"),
            leaf("05-lower-of-cost-and-nrv", "5.3.5", "lower-of-cost-and-nrv", "التكلفة أو صافي القيمة القابلة للتحقق أيهما أقل"),
        ]),
        node("04-inventory-analysis", "5.4", "inventory-analysis", "تحليل المخزون", [
            leaf("01-inventory-turnover", "5.4.1", "inventory-turnover", "معدل دوران المخزون"),
            leaf("02-gross-profit-ratio", "5.4.2", "gross-profit-ratio", "نسبة مجمل الربح"),
        ]),
    ]),
    node("06-long-term-assets", "6", "long-term-assets", "الأصول طويلة الأجل", [
        node("01-fixed-assets", "6.1", "fixed-assets", "الأصول الثابتة", [
            leaf("01-nature", "6.1.1", "nature", "طبيعة الأصول طويلة الأجل"),
            leaf("02-acquisition", "6.1.2", "acquisition", "اقتناء الأصول"),
            leaf("03-capitalization-vs-expense", "6.1.3", "capitalization-vs-expense", "الرسملة مقابل تحميل المصروف"),
            leaf("04-disposal", "6.1.4", "disposal", "التصرف في الأصول"),
        ]),
        node("02-depreciation", "6.2", "depreciation", "الإهلاك", [
            leaf("01-concept", "6.2.1", "concept", "مفهوم الإهلاك"),
            leaf("02-straight-line", "6.2.2", "straight-line", "طرق الإهلاك - القسط الثابت"),
            leaf("03-declining-balance", "6.2.3", "declining-balance", "طرق الإهلاك - الرصيد المتناقص"),
            leaf("04-units-of-production", "6.2.4", "units-of-production", "طرق الإهلاك - وحدات الإنتاج"),
            leaf("05-selection-and-change", "6.2.5", "selection-and-change", "اختيار وتغيير طريقة الإهلاك"),
            leaf("06-accounting-treatment", "6.2.6", "accounting-treatment", "المعالجة المحاسبية للإهلاك"),
        ]),
        node("03-special-topics-in-long-term-assets", "6.3", "special-topics-in-long-term-assets", "موضوعات خاصة بالأصول طويلة الأجل", [
            leaf("01-natural-resources-depletion", "6.3.1", "natural-resources-depletion", "إهلاك الموارد الطبيعية"),
            leaf("02-intangible-assets", "6.3.2", "intangible-assets", "الأصول غير الملموسة"),
            leaf("03-research-and-development", "6.3.3", "research-and-development", "البحث والتطوير"),
            leaf("04-tax-considerations", "6.3.4", "tax-considerations", "الاعتبارات الضريبية المرتبطة بالأصول"),
        ]),
    ]),
    node("07-financing-sources-and-liabilities", "7", "financing-sources-and-liabilities", "مصادر التمويل والالتزامات", [
        node("01-debt-financing", "7.1", "debt-financing", "التمويل بالديون", [
            leaf("01-loans", "7.1.1", "loans", "القروض"),
            leaf("02-bonds", "7.1.2", "bonds", "السندات"),
            leaf("03-interest", "7.1.3", "interest", "فوائد القروض والسندات"),
            leaf("04-issuance", "7.1.4", "issuance", "إصدار السندات"),
            leaf("05-discount-or-premium", "7.1.5", "discount-or-premium", "خصم أو علاوة إصدار السندات"),
            leaf("06-redemption", "7.1.6", "redemption", "سداد السندات"),
            leaf("07-finance-lease", "7.1.7", "finance-lease", "التأجير التمويلي"),
        ]),
        node("02-other-liabilities", "7.2", "other-liabilities", "الالتزامات الأخرى", [
            leaf("01-current-liabilities", "7.2.1", "current-liabilities", "الالتزامات الجارية"),
            leaf("02-contingent-liabilities", "7.2.2", "contingent-liabilities", "الالتزامات الطارئة"),
            leaf("03-deferred-taxes", "7.2.3", "deferred-taxes", "الضرائب المؤجلة"),
        ]),
        node("03-financing-structure-analysis", "7.3", "financing-structure-analysis", "تحليل هيكل التمويل", [
            leaf("01-debt-ratios", "7.3.1", "debt-ratios", "نسب المديونية"),
            leaf("02-ability-to-meet-obligations", "7.3.2", "ability-to-meet-obligations", "قدرة المنشأة على الوفاء بالالتزامات"),
        ]),
    ]),
    node("08-equity", "8", "equity", "حقوق الملكية", [
        node("01-equity-in-partnerships-and-sole-proprietorships", "8.1", "equity-in-partnerships-and-sole-proprietorships", "حقوق الملكية في شركات الأشخاص والمنشآت الفردية", [
            leaf("01-capital", "8.1.1", "capital", "رأس المال"),
            leaf("02-withdrawals", "8.1.2", "withdrawals", "السحب"),
            leaf("03-profit-and-loss-distribution", "8.1.3", "profit-and-loss-distribution", "توزيع الأرباح والخسائر"),
        ]),
        node("02-equity-in-joint-stock-companies", "8.2", "equity-in-joint-stock-companies", "حقوق الملكية في الشركات المساهمة", [
            leaf("01-common-shares", "8.2.1", "common-shares", "الأسهم العادية"),
            leaf("02-preferred-shares", "8.2.2", "preferred-shares", "الأسهم الممتازة"),
            leaf("03-treasury-shares", "8.2.3", "treasury-shares", "أسهم الخزينة"),
            leaf("04-reserves", "8.2.4", "reserves", "الاحتياطيات"),
            leaf("05-retained-earnings", "8.2.5", "retained-earnings", "الأرباح المحتجزة"),
            leaf("06-dividends", "8.2.6", "dividends", "توزيعات الأرباح"),
            leaf("07-earnings-per-share", "8.2.7", "earnings-per-share", "نصيب السهم من الأرباح"),
        ]),
        node("03-equity-in-non-profit-entities", "8.3", "equity-in-non-profit-entities", "حقوق الملكية في المنشآت غير الهادفة للربح", [
            leaf("01-concept-and-presentation", "8.3.1", "concept-and-presentation", "مفهوم حقوق الملكية وطريقة عرضها"),
        ]),
    ]),
    node("09-topics-affecting-profit-and-equity", "9", "topics-affecting-profit-and-equity", "موضوعات تؤثر على الربح وحقوق الملكية", [
        leaf("01-extraordinary-items", "9.1", "extraordinary-items", "البنود غير العادية"),
        leaf("02-discontinued-operations", "9.2", "discontinued-operations", "العمليات غير المستمرة"),
        leaf("03-changes-in-policies-or-principles", "9.3", "changes-in-policies-or-principles", "التغير في السياسات أو المبادئ المحاسبية"),
        leaf("04-retained-earnings-adjustments", "9.4", "retained-earnings-adjustments", "تسويات الأرباح المحتجزة"),
        leaf("05-pensions-and-post-retirement-benefits", "9.5", "pensions-and-post-retirement-benefits", "المعاشات ومنافع ما بعد التقاعد"),
        leaf("06-income-taxes", "9.6", "income-taxes", "ضرائب الدخل"),
    ]),
    node("10-investment-merger-and-consolidation", "10", "investment-merger-and-consolidation", "الاستثمار والاندماج والقوائم المجمعة", [
        node("01-accounting-for-investments", "10.1", "accounting-for-investments", "المحاسبة عن الاستثمارات", [
            leaf("01-cost-method", "10.1.1", "cost-method", "طريقة التكلفة"),
            leaf("02-fair-value-method", "10.1.2", "fair-value-method", "طريقة القيمة العادلة"),
            leaf("03-equity-method", "10.1.3", "equity-method", "طريقة حقوق الملكية"),
        ]),
        node("02-mergers-and-acquisitions", "10.2", "mergers-and-acquisitions", "الاندماج والاستحواذ", [
            leaf("01-types-of-mergers", "10.2.1", "types-of-mergers", "أشكال الاندماج"),
            leaf("02-goodwill", "10.2.2", "goodwill", "الشهرة"),
            leaf("03-goodwill-measurement", "10.2.3", "goodwill-measurement", "قياس الشهرة ومعالجتها"),
            leaf("04-purchase-method", "10.2.4", "purchase-method", "طريقة الشراء"),
            leaf("05-pooling-of-interests", "10.2.5", "pooling-of-interests", "طريقة المصالح المشتركة"),
        ]),
        node("03-consolidated-financial-statements", "10.3", "consolidated-financial-statements", "القوائم المالية المجمعة", [
            leaf("01-consolidation-concept", "10.3.1", "consolidation-concept", "مفهوم التجميع"),
            leaf("02-consolidation-procedures", "10.3.2", "consolidation-procedures", "أسس وإجراءات التجميع"),
            leaf("03-elimination-of-intercompany-transactions", "10.3.3", "elimination-of-intercompany-transactions", "استبعاد العمليات المتبادلة"),
            leaf("04-valuation-of-assets-and-liabilities", "10.3.4", "valuation-of-assets-and-liabilities", "تقييم الأصول والالتزامات"),
        ]),
    ]),
    node("11-foreign-currency", "11", "foreign-currency", "العملات الأجنبية", [
        leaf("01-foreign-currency-transactions", "11.1", "foreign-currency-transactions", "العمليات بالعملة الأجنبية"),
        leaf("02-exchange-rate-differences", "11.2", "exchange-rate-differences", "فروق أسعار الصرف"),
        leaf("03-translation-of-financial-statements", "11.3", "translation-of-financial-statements", "ترجمة القوائم المالية"),
        leaf("04-disclosure-under-ias21", "11.4", "disclosure-under-ias21", "الإفصاح وفق IAS 21"),
    ]),
    node("12-financial-analysis", "12", "financial-analysis", "التحليل المالي", [
        leaf("01-horizontal-analysis", "12.1", "horizontal-analysis", "التحليل الأفقي"),
        leaf("02-vertical-analysis", "12.2", "vertical-analysis", "التحليل الرأسي"),
        leaf("03-liquidity-ratios", "12.3", "liquidity-ratios", "نسب السيولة"),
        leaf("04-activity-ratios", "12.4", "activity-ratios", "نسب النشاط"),
        leaf("05-profitability-ratios", "12.5", "profitability-ratios", "نسب الربحية"),
        leaf("06-debt-ratios", "12.6", "debt-ratios", "نسب المديونية"),
        leaf("07-working-capital", "12.7", "working-capital", "رأس المال العامل"),
        leaf("08-return-on-investment", "12.8", "return-on-investment", "العائد على الاستثمار"),
        leaf("09-relationship-between-ratios", "12.9", "relationship-between-ratios", "العلاقة بين النسب المالية"),
        leaf("10-limitations-of-financial-analysis", "12.10", "limitations-of-financial-analysis", "حدود التحليل المالي"),
    ]),
    node("13-measurement-and-disclosure-theories", "13", "measurement-and-disclosure-theories", "نظريات القياس والإفصاح", [
        node("01-accounting-measurement-methods", "13.1", "accounting-measurement-methods", "أساليب القياس المحاسبي", [
            leaf("01-historical-cost", "13.1.1", "historical-cost", "التكلفة التاريخية"),
            leaf("02-fair-value", "13.1.2", "fair-value", "القيمة العادلة"),
            leaf("03-replacement-cost", "13.1.3", "replacement-cost", "تكلفة الاستبدال"),
            leaf("04-net-realizable-value", "13.1.4", "net-realizable-value", "صافي القيمة القابلة للتحقق"),
        ]),
        node("02-profit-and-capital-maintenance-theories", "13.2", "profit-and-capital-maintenance-theories", "نظريات الربح والمحافظة على رأس المال", [
            leaf("01-financial-capital-maintenance", "13.2.1", "financial-capital-maintenance", "المحافظة على رأس المال النقدي"),
            leaf("02-physical-capital-maintenance", "13.2.2", "physical-capital-maintenance", "المحافظة على رأس المال المادي"),
            leaf("03-effect-on-profit", "13.2.3", "effect-on-profit", "أثر كل منهما على الربح"),
        ]),
        node("03-disclosure-and-financial-reporting", "13.3", "disclosure-and-financial-reporting", "الإفصاح والتقارير المالية", [
            leaf("01-agency-theory", "13.3.1", "agency-theory", "نظرية الوكالة"),
            leaf("02-agency-cost", "13.3.2", "agency-cost", "تكلفة الوكالة"),
            leaf("03-annual-report", "13.3.3", "annual-report", "التقرير السنوي"),
            leaf("04-board-report", "13.3.4", "board-report", "تقرير مجلس الإدارة"),
            leaf("05-governance-report", "13.3.5", "governance-report", "تقرير الحوكمة"),
            leaf("06-social-responsibility-report", "13.3.6", "social-responsibility-report", "تقرير المسؤولية الاجتماعية"),
            leaf("07-auditor-report", "13.3.7", "auditor-report", "تقرير مراجع الحسابات"),
            leaf("08-management-notes", "13.3.8", "management-notes", "ملاحظات الإدارة"),
        ]),
    ]),
]


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8-sig")


def make_leaf_files(folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    for filename in ["theory.md", "examples.md", "essay.md", "mistakes.md"]:
        (folder / filename).write_text("", encoding="utf-8-sig")
    (folder / "mcq.json").write_text("[]\n", encoding="utf-8-sig")


def write_node(parent: Path, item: dict, order: int) -> None:
    folder = parent / item["folder"]
    folder.mkdir(parents=True, exist_ok=True)

    if item.get("leaf"):
        make_leaf_files(folder)
        write_json(
            folder / "meta.json",
            {
                "code": item["code"],
                "title": item["title"],
                "slug": item["slug"],
                "order": order,
                "tabs": TABS,
            },
        )
        return

    declared_children = []
    for child_order, child in enumerate(item["children"], start=1):
        declared_children.append(
            {"code": child["code"], "slug": child["slug"], "title": child["title"], "order": child_order}
        )
        write_node(folder, child, child_order)

    write_json(
        folder / "meta.json",
        {
            "code": item["code"],
            "title": item["title"],
            "slug": item["slug"],
            "order": order,
            "children": declared_children,
        },
    )


def main() -> None:
    if CONTENT_DIR.exists():
        shutil.rmtree(CONTENT_DIR)
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    for order, item in enumerate(TREE, start=1):
        write_node(CONTENT_DIR, item, order)

    print("Content structure regenerated using parent/topics or parent/child/topics only.")


if __name__ == "__main__":
    main()
